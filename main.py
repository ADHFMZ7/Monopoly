from game import Game 

if __name__ == "__main__":
    
    game = Game()    


    while True: # replace with game condition function
        
        for player in game.get_players():
             game.take_turn(player)
             
