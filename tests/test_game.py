import sys
import os
import pytest
from unittest.mock import patch

# Додавання шляху до каталогу верхнього рівня
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.player import Player

def test_player_choice():
    player = Player()
    options = ["rock", "paper", "scissors", "lizard", "spock"]

    with patch('builtins.input', return_value='rock'):
        choice = player.choose_option(options)
        assert choice in options

# Якщо у вас є ще тести, додайте їх тут аналогічним чином.
