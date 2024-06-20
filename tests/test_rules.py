import sys
import os
import pytest

# Додавання шляху до каталогу верхнього рівня
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.rules import determine_winner

def test_determine_winner():
    assert determine_winner("rock", "scissors") == "You win!"
    assert determine_winner("rock", "rock") == "It's a tie!"
    assert determine_winner("rock", "paper") == "Computer wins!"

# Якщо у вас є ще тести, додайте їх тут аналогічним чином.
