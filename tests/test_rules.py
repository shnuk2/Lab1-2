import sys
import os
import pytest

# Додавання шляху до каталогу верхнього рівня
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from game.rules import determine_winner

# Фікстури
@pytest.fixture
def options():
    return ["rock", "paper", "scissors", "lizard", "spock"]

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

@pytest.mark.slow
def test_slow_operation():
    import time
    time.sleep(1)
    assert True

@pytest.mark.skip(reason="This test is skipped for demonstration purposes.")
def test_skipped():
    assert False
