

class Game:
    
    def __init__(self):
        self.players = []
        self.board =  None
        
        self.init_board()
       
    def get_players(self):
        return self.players
       
    def take_turn(self, player):
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

class Property:
   pass 

class Bank:
   pass 