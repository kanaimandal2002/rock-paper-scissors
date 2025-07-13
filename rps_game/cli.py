from .game import RockPaperScissors, Choice
import argparse

def parse_choice(choice_str: str) -> Choice:
    """Convert user input string to Choice enum."""
    choice_map = {
        'rock': Choice.ROCK,
        'paper': Choice.PAPER,
        'scissors': Choice.SCISSORS,
        'r': Choice.ROCK,
        'p': Choice.PAPER,
        's': Choice.SCISSORS
    }
    return choice_map.get(choice_str.lower())

def print_result(result):
    """Print the result of a game round."""
    outcome = {
        'win': "You win!",
        'lose': "You lose!",
        'tie': "It's a tie!"
    }[result.result]
    
    print(f"\nYou chose: {result.user_choice.name.lower()}")
    print(f"Computer chose: {result.computer_choice.name.lower()}")
    print(outcome)

def main():
    game = RockPaperScissors()
    
    print("Welcome to Rock-Paper-Scissors!")
    print("Enter 'rock' (r), 'paper' (p), 'scissors' (s), or 'quit' to exit.")
    
    while True:
        user_input = input("\nYour choice: ").strip()
        
        if user_input.lower() in ('quit', 'q', 'exit'):
            break
            
        try:
            user_choice = parse_choice(user_input)
        except (KeyError, AttributeError):
            print("Invalid choice. Please enter rock, paper, or scissors.")
            continue
            
        result = game.play_round(user_choice)
        print_result(result)
        
        stats = game.get_stats()
        print(f"\nStats - Wins: {stats['wins']}, Losses: {stats['losses']}, Ties: {stats['ties']}")
    
    stats = game.get_stats()
    print("\nFinal Statistics:")
    print(f"Total games: {stats['total']}")
    print(f"Wins: {stats['wins']} ({stats['wins']/stats['total']:.1%})")
    print(f"Losses: {stats['losses']} ({stats['losses']/stats['total']:.1%})")
    print(f"Ties: {stats['ties']} ({stats['ties']/stats['total']:.1%})")

if __name__ == "__main__":
    main()
