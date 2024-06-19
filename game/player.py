import random

class Player:
    def __init__(self, is_computer=False):
        self.is_computer = is_computer

    def choose_option(self, options):
        if self.is_computer:
            return random.choice(options)
        else:
            while True:
                choice = input(f"Choose one ({', '.join(options)}): ").lower()
                if choice in options:
                    return choice
                print("Invalid choice, try again.")
