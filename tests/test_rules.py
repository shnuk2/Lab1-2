import unittest
from game.rules import determine_winner

class TestRules(unittest.TestCase):
    def test_determine_winner(self):
        self.assertEqual(determine_winner("rock", "scissors"), "You win!")
        self.assertEqual(determine_winner("rock", "rock"), "It's a tie!")
        self.assertEqual(determine_winner("rock", "paper"), "Computer wins!")

if __name__ == "__main__":
    unittest.main()
