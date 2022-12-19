from game import Game 

if __name__ == "__main__":
    
    game = Game()    


    while not game.win():
        
        for player in game.get_players():
            if player.jail in [1, 2, 3, 4]:
                player.jail_turn()
            else:
                player.take_turn()
    print(f"{game.win().name} wins!")
            
             

