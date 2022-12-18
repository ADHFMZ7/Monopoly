from game import Game 

if __name__ == "__main__":
    
    game = Game()    


    while not game.win(): # replace with game condition function
        
        for player in game.get_players():
            if player.jail:
                player.jail_turn()
            else:
                player.take.take_turn()
            
             


"""
Every turn we need to make sure 


"""
          
    
             
