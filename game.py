import random
from data import BOARD, PROPERTIES
import dataclasses

class Game:
    
    def __init__(self):
        self.players = []
        self.board = BOARD
        self.init_board()
    
    def init_board(self):

        num_players = int(input("Enter number of players: "))

        for i in range(num_players):
            name = input(f"Enter name for player {i + 1}: ")
            self.players.append(Player(name, i)) 
       
    def get_players(self):
        return self.players
  
    def win(self):
        if len(self.players) <= 1:
            return True
        
   
class Player:
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.space = 0
        self.money = 1500
        self.properties = []
        self.jail = 0
        self.double = 0

    def take_turn(self):
        self.print_info() 
        input("Press enter to roll dice\n")
        d1, d2 = [random.randint(1, 6) for _ in range(2)]
        input(f"{self.name} rolled a {d1} and a {d2}\nPress enter to continue")

        self.move(d1+d2)
        if d1 == d2 and self.double < 3:
            self.double += 1
            input("You rolled a double")
            self.take_turn(self)
            return
        elif self.double >= 3:
            self.double = 0
            print("You rolled 3 doubles. You are in jail!")
        else:
            self.double = 0 
        
    def print_info(self):
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
            
        spot = BOARD[self.space]
        
        if spot == "Community Chest":
            self.chest()
            
        elif spot == "Chance":
            self.change()
        
        elif spot in  ["Free Parking", "GO", "Jail"]:
            print(f"You landed on {spot}. Do nothing.")
            pass
        
        elif spot == "Luxury Tax":
            print("You landed on Luxury Tax. pay $100")
            self.pay(100, 'bank')
            
        elif spot == "Income Tax":
            print("You landed on Income Tax. play $200")
            self.pay(200, 'bank')
        
        elif spot == "Go to Jail":
            self.goto_jail()
        
        else:
            print(f"You landed on: {spot}")
            if self.money >= PROPERTIES[spot]["price"]:
                if int(input("Would you like to purchase this property? 0/1: ")):
                    self.buy(spot)
                    print(f"{spot} has been purchased.")
        
        # LIST OPTIONS
        
        # BUY PROPERTY IF IT IS BUYABLE
        # BUY HOUSES/HOTELS
                
                    
            
    def buy(self, square):
        self.properties.append(square)
        self.pay(PROPERTIES[square]["price"], 'bank')
            
    def pay(self, amount, reciever):
        if self.money < amount:
            self.bankrupt() 
        else:
            self.money -= amount
            if reciever != "bank":
                reciever.money += amount

    def goto_jail(self):
        self.space = BOARD.index('Jail')
        self.jail = 1

    def bankrupt(self, recipient, debt):
        if self.money < debt:
            for i in self.properties:
                self.sell_property(i)

    def sell_property(self, property):
        self.money += 0.5 * PROPERTIES[property]["price"]

class Bank:
    pass

class Property:
    def __init__(self, name, owner):
        self.name = name
        self.owner = ''
        