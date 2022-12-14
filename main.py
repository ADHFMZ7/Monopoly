import random

class MonopolyGame:
  def __init__(self):
    self.board = [
      "GO", "Mediterranean Avenue", "Community Chest", "Baltic Avenue",
      "Income Tax", "Reading Railroad", "Oriental Avenue", "Chance",
      "Vermont Avenue", "Connecticut Avenue", "Jail", "St. Charles Place",
      "Electric Company", "States Avenue", "Virginia Avenue", "Pennsylvania Railroad",
      "St. James Place", "Community Chest", "Tennessee Avenue", "New York Avenue",
      "Free Parking", "Kentucky Avenue", "Chance", "Indiana Avenue",
      "Illinois Avenue", "B. & O. Railroad", "Atlantic Avenue", "Ventnor Avenue",
      "Water Works", "Marvin Gardens", "Go To Jail", "Pacific Avenue",
      "North Carolina Avenue", "Community Chest", "Pennsylvania Avenue", "Short Line Railroad",
      "Chance", "Park Place", "Luxury Tax", "Boardwalk"
    ]

    self.chest_cards = [
      "Advance to Go (Collect $200)", "Bank error in your favor – Collect $75",
      "Doctor's fees – Pay $50", "From sale of stock you get $50",
      "Get Out of Jail Free – This card may be kept until needed",
      "Go to Jail – Go directly to jail – Do not pass Go – Do not collect $200",
      "Grand Opera Night – Collect $50 from every player for opening night seats",
      "Holiday Fund matures – Receive $100", "Income tax refund – Collect $20",
      "It is your birthday – Collect $10 from each player",
      "Life insurance matures – Collect $100", "Pay hospital fees of $100",
      "Pay school fees of $150", "Receive $25 consultancy fee",
      "You are assessed for street repairs – $40 per house – $115 per hotel",
      "You have won second prize in a beauty contest – Collect $10",
      "You inherit $100"
    ]

    self.chance_cards = [
      "Advance to Go (Collect $200)", "Advance to Illinois Ave.",
      "Advance to St. Charles Place – If you pass Go, collect $200",
      "Advance to nearest Utility", "Advance to the nearest Railroad",
      "Bank pays you dividend of $50", "Get Out of Jail Free – This card may be kept until needed",
      "Go back three spaces", "Go to Jail – Go directly to jail – Do not pass Go – Do not collect $200",
      "Make general repairs on all your property – For each house pay $25 – For each hotel $100",
      "Pay poor tax of $15", "Take a trip to Reading Railroad – If you pass Go, collect $200",
      "Take a walk on the Boardwalk – Advance to Boardwalk",
      "You have been elected Chairman of the Board – Pay each player $50",
      "Your building and loan matures – Receive $150",
      "You have won a crossword competition – Collect $100"
    ]

    self.players = []
    self.current_player = 0

  def add_player(self, name):
    self.players.append(Player(name))

  def get_current_player(self):
    return self.players[self.current_player]

  def roll_dice(self):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

  def move_player(self, player, dice):
    player.current_position += sum(dice)
    if player.current_position >= len(self.board):
      player.current_position -= len(self.board)
      player.money += 200

  def perform_action(self, player):
    current_space = self.board[player.current_position]

    if current_space == "Community Chest":
      card = random.choice(self.chest_cards)
      if card.startswith("Advance to"):
        new_pos = self.board.index(card.split(" ")[-1])
        player.current_position = new_pos
        self.perform_action(player)
      elif card.startswith("Go to Jail"):
        player.current_position = self.board.index("Jail")
      elif card.endswith("Collect $"):
        amount = int(card.split("$")[-1])
        player.money += amount
      elif card.endswith("Pay $"):
        amount = int(card.split("$")[-1])
        player.money -= amount

    elif current_space == "Chance":
      card = random.choice(self.chance_cards)
      if card.startswith("Advance to"):
        new_pos = self.board.index(card.split(" ")[-1])
        player.current_position = new_pos
        self.perform_action(player)
      elif card.startswith("Go to Jail"):
        player.current_position = self.board.index("Jail")
      elif card.endswith("Collect $"):
        amount = int(card.split("$")[-1])
        player.money += amount
      elif card.endswith("Pay $"):
        amount = int(card.split("$")[-1])
        player.money -= amount

    elif current_space.endswith("Railroad"):
      player.money -= 200
      player.railroads += 1

    elif current_space == "Jail":
      pass

    elif current_space == "Free Parking":
      pass

    elif current_space == "Go To Jail":
      player.current_position = self.board.index("Jail")

    elif current_space.endswith("Utility"):
      player.money -= 50
      player.utilities += 1

    elif current_space.endswith("Avenue"):
      player.money -= 100
      player.properties.append(current_space)

    elif current_space.endswith("Place"):
      player.money -= 150
      player.properties.append(current_space)

  def play_round(self):
    player = self.get_current_player()
    dice = self.roll_dice()
    self.move_player(player, dice)
    self.perform_action(player)
    self.current_player = (self.current_player + 1) % len(self.players)

    
  def play_game(self):
    while True:
      self.play_round()
      if self.is_game_over():
        break

  def is_game_over(self):
    for player in self.players:
      if player.money < 0:
        return True
    return False


class Player:
  def __init__(self, name):
    self.name = name
    self.money = 1500
    self.current_position = 0
    self.properties = []
    self.railroads = 0
    self.utilities = 0


# Initialize game and add players
game = MonopolyGame()
game.add_player("Player 1")
game.add_player("Player 2")

# Play game
game.play_game()

