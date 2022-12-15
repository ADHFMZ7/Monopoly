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

        d1, d2 = [rand.randint(1, 6) for _ in range(2)]
        self.move(player, d1+d2)
        if d1 == d2:
            double += 1
        
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

        
     

class Property:
   pass 

class Bank:
   pass 
