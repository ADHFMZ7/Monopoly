# Monopoly
CS 335 Algorithms project

This program implements the popular board game Monopoly using the console.
The console has some limitations, so some features of the original game have been tweaked.

- Auctioning away properties is not included because it is difficult in a console application.
- The player having to charge rent themselves is removed. Instead it is automatically deducted.
- Selling properties to other players is also removed. The player can only sell to the bank when bankruptcy is reached.

# The Classes

The game works with two main classes of objects; The main Game class, and the Player class.

## Game Class

- __init__(self): This method initializes the board by prompting the players for the amount of player. It then creates a Player object for each one.
- get_players(self): This method returns a list of the players.
- win(self): This method returns True if the win conditions are met.
- remove_player(self): This method removes a player. It is used when a player goes bankrupt.

## Player Class

- __init__(self, name, number, game): This is the constructor. It takes in a name, the player number, and the game object to create a new player.
- take_turn(self): This method takes a turn
- print_info(self): This method prints out the important information of the player class.
- move(self, number): Moves the player the desired number of spaces.
- rand_card(self): This function generates a random card to be used for chance and Community Chest cards.
- evaluate_square(self): This board gets the current square the player is on and takes the actions necessary.
- jail_turn(self): This function takes a turn if the player is in jail.
- buy(self, square): This function buys the property on the specified square.
- buy_houses(self, prop): This function buys a house on the specified property. If there are 4 houses, it promotes them to a hotel. 
- pay(self, amount, reciever): This function pays the desired amount to another player or the bank. If the player cannot afford the debt, the player declares bankrupt.
- goto_jail(self): This moves the player to jail and starts the turn counter.
- bankrupt(self, recipient, debt): This function sells all of the players assets at half their price. It then pays the player that is owed the desired amount. It then removes the player that declared bankrupt from the game.
- sell_property(self, property): This sells the desired property and all of the buildings on it back to the bank for half the price.
- pay_rent(self): The pay_rent function pays the rent that is owed from being on a square. It pays the rent to the player that owns the square.

