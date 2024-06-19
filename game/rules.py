def determine_winner(player_choice, computer_choice):
    winning_combinations = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }

    if player_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in winning_combinations[player_choice]:
        return "You win!"
    else:
        return "Computer wins!"
