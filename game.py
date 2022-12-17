import random

class Game:
    
    def __init__(self):
        self.players = []
        self.board =  None
        self.positions = {} 
        self.init_board()
       
    def get_players(self):
        return self.players
       
    def take_turn(self, player):

        player.print_info() 
        input("Press enter to roll dice")
        d1, d2 = [random.randint(1, 6) for _ in range(2)]
        #self.move(player, d1+d2)
        print(f"{player.name} rolled {d1} and {d2}") 
        if d1 == d2 and player.double < 3:
            player.double += 1
            self.take_turn(player)
            input("You rolled a double")
            return
        elif player.double >= 3:
            player.double = 0
            print("You rolled 3 doubles. You are in jail!")
        else:
            player.double = 0
            
        
    def move():
       pass 
     
    def init_board(self):
    
        num_players = int(input("Enter number of players: "))
        
        for i in range(num_players):
            name = input(f"Enter name for player {i + 1}: ")
            self.players.append(Player(name)) 

class Player:
    
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.properties = []
        self.jail = False
        self.double = 0
        self.space = 0

        
    def print_info(self):
      print(f"{self.name}'s turn")
      print(f"Space #: {self.space}")
      print(f"Money left: {self.money}")
      # print properties 

class Property:
   pass 

class Bank:
   pass 
