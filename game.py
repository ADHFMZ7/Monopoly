import random
from data import BOARD, PROPERTIES


class Game:
    
    def __init__(self):
        self.players = []
        self.board = BOARD
        self.init_board()
    
    def init_board(self):

        num_players = int(input("Enter number of players: "))

        for i in range(num_players):
            name = input(f"Enter name for player {i + 1}: ")
            self.players.append(Player(name, i, self)) 
        for i in PROPERTIES:
            PROPERTIES[i]["owner"] = None
       
    def get_players(self):
        return self.players
  
    def win(self):
        if len(self.players) <= 1:
            return self.players[0]
    
    def remove_player(self, player):
        self.get_players().remove(player)
        
   
class Player:
    
    def __init__(self, name, number, game):
        self.name = name
        self.number = number
        self.space = 0
        self.money = 1500
        self.properties = []
        self.jail = 0
        self.card = 0
        self.game = game
        self.railroads = 0

    def take_turn(self):
        double = 0
        while True:
            self.print_info() 
            input("Press enter to roll dice\n")
            d1, d2 = [random.randint(1, 6) for _ in range(2)]
            input(f"{self.name} rolled a {d1} and a {d2}\nPress enter to continue")
            self.move(d1+d2)
            self.evaluate_square()
            self.pay_rent()
            if BOARD[self.space] == "Jail":
                break
            if self.game.win():
                return
            if d1 == d2 and double < 3:
                double += 1
                input("You rolled a double")
                continue    
            elif double >= 3:
                double = 0
                print("You rolled 3 doubles. You are in jail!")
                break
            else:
                break
        
    def print_info(self):
        print("\n") 
        print("="*30)
        print(f"{self.name}'s turn")
        print(f"Space #: {self.space}")
        print(f"Money left: {self.money}")
        print(f"Properties: {self.properties}")
        
    def move(self, number):
        if number + self.space >= 40:
            print("You Passed GO. collect 200")
            self.space = (self.space + number) - 40
            self.money += 200
        else:
            self.space += number
           
    def rand_card(self):
        number = random.randint(1, 115)
        if number % 2 and number < 100:
            print(f"Collect ${2 * number}")
            self.money += 2 * number
        elif not number % 2 and number < 100:
            print(f"Pay ${number}")
            self.pay(number, 'bank')
        else:
            print("You got a get out of jail free card.")
            self.card += 1
            
            
    def evaluate_square(self):
        spot = BOARD[self.space]
        print(f"You landed on {spot}")
        buyable = False
        if spot in ["Community Chest", "Chance"]: 
            self.rand_card()
        
        elif spot in  ["Free Parking", "GO", "Jail"]:
            print("Do nothing.")
            pass
        
        elif spot == "Luxury Tax":
            print("pay $100")
            self.pay(100, 'bank')
            
        elif spot == "Income Tax":
            print("pay $200")
            self.pay(200, 'bank')
        
        elif spot == "Go to Jail":
            print("Go to jail")
            self.goto_jail()
            
        elif spot in PROPERTIES.keys() and not PROPERTIES[spot]["owner"]:
            buyable = True
        
        turn = True 
        while True:
            print("\nOptions:")
            print("1. End turn")
            print("2. Buy houses/hotels")
            if buyable:
                print("3. buy property")
            try:
                option = int(input("Option: "))
            except:
                continue
            if option == 1:
                break
            elif option == 2:
                
                print("Which property?")
                temp = [i for i in self.properties if not i.endswith("Railroad") and i not in ["Water Works", "Electric Company"]]
                for i, prop in enumerate(temp):
                    print(f"{i} for {prop}") 
                try:
                    if not self.properties:
                        print("No properties")
                        continue
                    prop = temp[int(input("Property: "))]
                except:
                    continue
                self.buy_houses(prop)
            elif option == 3 and buyable:
                if self.money >= PROPERTIES[spot]["price"]:
                    self.buy(spot)
                    buyable = False
                else:
                    print("Cannot afford property")
            else:
                print("Invalid input. please continue.")
                
            
    def jail_turn(self):
        self.print_info() 
        if self.jail == 4:
            print("You have been in jail for 3 turns. you must pay $50")
            self.pay(50, 'bank') 
            self.jail = 0
            if not self.game.win():
                print("You are now out of jail!")
                self.take_turn()
            return
        while True:
            self.jail += 1
            
            
            
            print("\nYou are in jail.")
            print("type 1 to pay 50 and exit")
            print("type 2 to roll dice")
            print("type 3 to use a get out of jail card")  
            try:
                prompt = int(input("enter option: ")) 
            except:
                print("Invalid choice. Try again")
                continue
        
            if prompt not in [1, 2, 3]:
                print("Invalid choice. Try again.")
                continue


            if prompt == 1:
                if self.money >= 50:
                    self.pay(50, 'bank')
                    self.jail = 0
                    print("You are now out of jail!")
                    break
                else:
                    print("You do not have enough money")
                    continue
            elif prompt == 2:
                d1, d2 = [random.randint(1, 6) for _ in range(2)]
                print(f"You rolled a {d1} and a {d2}")
                if d1 == d2:
                    self.jail = 0
                    self.move(d1 + d2)
                    print("You are now out of jail!") 
                else:
                    print(f"You are still in jail.")
                break
                    
            elif prompt == 3:
                if self.card >= 1:
                    self.jail = 0
                    self.card -= 1
                    print("You are now out of jail!")
                    break
                else:
                    print("You do not have any get out of jail cards")
                    continue
            else:
                print("Invalid choice. Try again.")    
                continue
             
                
    def buy(self, square):
        if square.endswith("Railroad"):
            self.railroads += 1
        if square in ["Electric Company", "Water Works"]:
            self.railroads+= 1
        self.properties.append(square)
        PROPERTIES[square]["owner"] = self
        PROPERTIES[square]["houses"] = 0
        self.pay(PROPERTIES[square]["price"], 'bank')
        print(f"{square} has been purchased")
        
    def buy_houses(self, prop):
        if PROPERTIES[prop]["houses"] >= 4:
            if PROPERTIES[prop]["houses"] >= 5:
                print("Reached maximum amount of houses/hotels")
            elif self.money >= PROPERTIES[prop]["hotel_cost"]:
                self.pay(PROPERTIES[prop]["hotel_cost"], 'bank')
                PROPERTIES[prop]["houses"] += 1
                print(f"Bought one hotel for {prop}")
            else:
                print("Cannot afford hotel")
        else:
            if self.money >= PROPERTIES[prop]["house_cost"]:
                self.pay(PROPERTIES[prop]["house_cost"], 'bank')
                PROPERTIES[prop]["houses"] += 1
                print(f"Bought one house for {prop}")
            else:
                print("Cannot afford house")
        
        
    def pay(self, amount, reciever):
        if self.money < amount:
            self.bankrupt(reciever, amount) 
        else:
            self.money -= amount
            if reciever != "bank":
                reciever.money += amount

    def goto_jail(self):
        self.space = BOARD.index('Jail')
        self.jail = 1

    def bankrupt(self, recipient, debt):
        print(f"{self.name} has gone bankrupt. They will be removed from the game")
        if self.money < debt:
            for i in self.properties:
                self.sell_property(i)

            print(f"Their remaining balance of {self.money} after selling their property has been given to {recipient}")
            self.pay(self.money, recipient)
        self.game.remove_player(self)

    def sell_property(self, property):
        if not property.endswith("Railroad") and property not in ["Water Works", "Electric Company"]:
            if PROPERTIES[property]["houses"] >= 5:
                self.money += 0.5 * PROPERTIES[property]["hotel_cost"]
                PROPERTIES[property]["houses"] -= 1
            self.money += 0.5 * PROPERTIES[property]["houses"] * PROPERTIES[property]["hotel_cost"]
            PROPERTIES[property]["houses"] = 0
        PROPERTIES[property]["owner"] = None
        self.money += 0.5 * PROPERTIES[property]["price"]

    def pay_rent(self):
        spot = BOARD[self.space]

            
        if spot in PROPERTIES.keys() and PROPERTIES[spot]["owner"] and PROPERTIES[spot]["owner"] != self:
            if spot.endswith("Railroad") or spot in ["Water Works", "Electric Company"]:
                self.pay(PROPERTIES[spot]["rent"][PROPERTIES[spot]["owner"].railroads], PROPERTIES[spot]["owner"])
                return
            self.pay(PROPERTIES[spot]["rent"][PROPERTIES[spot]["houses"]], PROPERTIES[spot]["owner"])
         