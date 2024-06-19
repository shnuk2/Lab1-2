from game.rules import determine_winner
from game.player.py import Player

class Game:
    def __init__(self):
        self.options = ["rock", "paper", "scissors", "lizard", "spock"]

    def start(self):
        print("Welcome to Rock Paper Scissors Lizard Spock!")
        player = Player()
        computer = Player(is_computer=True)
        
        player_choice = player.choose_option(self.options)
        computer_choice = computer.choose_option(self.options)
        
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(player_choice, computer_choice)
        print(winner)
