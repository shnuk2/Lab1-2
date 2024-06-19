import unittest
from game.player import Player
from game.rules import determine_winner

class TestGame(unittest.TestCase):
    def test_player_choice(self):
        player = Player()
        options = ["rock", "paper", "scissors", "lizard", "spock"]
        choice = player.choose_option(options)
        self.assertIn(choice, options)

if __name__ == "__main__":
    unittest.main()
