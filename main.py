from game import Game 

if __name__ == "__main__":
    
    game = Game()    


    while not game.win(): # replace with game condition function
        
        for player in game.get_players():
            if player.jail in range(1,3):
                player.jail_turn()
            else:
                player.take_turn()
    print(f"{game.win().name} wins!")
            
             


"""
Every turn we need to make sure 


"""
          
    
             
