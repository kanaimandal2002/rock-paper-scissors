import random
from dataclasses import dataclass
from enum import Enum, auto

class Choice(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

@dataclass
class GameResult:
    user_choice: Choice
    computer_choice: Choice
    result: str  # 'win', 'lose', or 'tie'

class RockPaperScissors:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def play_round(self, user_choice: Choice) -> GameResult:
        """Play one round of the game."""
        computer_choice = random.choice(list(Choice))
        
        if user_choice == computer_choice:
            result = 'tie'
            self.ties += 1
        elif (
            (user_choice == Choice.ROCK and computer_choice == Choice.SCISSORS) or
            (user_choice == Choice.PAPER and computer_choice == Choice.ROCK) or
            (user_choice == Choice.SCISSORS and computer_choice == Choice.PAPER)
        ):
            result = 'win'
            self.wins += 1
        else:
            result = 'lose'
            self.losses += 1
            
        return GameResult(user_choice, computer_choice, result)

    def get_stats(self) -> dict:
        """Return current game statistics."""
        return {
            'wins': self.wins,
            'losses': self.losses,
            'ties': self.ties,
            'total': self.wins + self.losses + self.ties
        }
