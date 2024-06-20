import sys
import os
import pytest
from unittest.mock import patch

# Додавання шляху до каталогу верхнього рівня
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.player import Player
from game.rules import determine_winner

# Фікстури
@pytest.fixture
def player():
    return Player()

@pytest.fixture
def options():
    return ["rock", "paper", "scissors", "lizard", "spock"]

# Тести для Player
@pytest.mark.parametrize("mock_input, expected_choice", [
    ('rock', 'rock'),
    ('paper', 'paper'),
    ('scissors', 'scissors'),
    ('lizard', 'lizard'),
    ('spock', 'spock'),
])
def test_player_choice(mock_input, expected_choice, player, options):
    with patch('builtins.input', return_value=mock_input):
        choice = player.choose_option(options)
        assert choice == expected_choice

@pytest.mark.slow
def test_slow_operation():
    import time
    time.sleep(1)
    assert True

@pytest.mark.skip(reason="This test is skipped for demonstration purposes.")
def test_skipped():
    assert False

# Тести для determine_winner
@pytest.mark.parametrize("player_choice, computer_choice, expected_result", [
    ("rock", "scissors", "You win!"),
    ("rock", "rock", "It's a tie!"),
    ("rock", "paper", "Computer wins!"),
    ("paper", "rock", "You win!"),
    ("scissors", "paper", "You win!"),
    ("lizard", "spock", "You win!"),
    ("spock", "scissors", "You win!"),
])
def test_determine_winner(player_choice, computer_choice, expected_result):
    result = determine_winner(player_choice, computer_choice)
    assert result == expected_result

@pytest.mark.xfail
def test_expected_failure():
    assert determine_winner("rock", "spock") == "You win!"
