from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

class Game:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
    
    def play_round(self, user_choice):
        options = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(options)
        result = self.determine_winner(user_choice, computer_choice)
        
        if result == 'win':
            self.wins += 1
        elif result == 'lose':
            self.losses += 1
        else:
            self.ties += 1
            
        return {
            'computer_choice': computer_choice,
            'result': result,
            'score': {
                'wins': self.wins,
                'losses': self.losses,
                'ties': self.ties
            }
        }
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'tie'
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            return 'win'
        else:
            return 'lose'

game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.json['choice']
    result = game.play_round(user_choice)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
