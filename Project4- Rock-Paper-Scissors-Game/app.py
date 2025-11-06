from flask import Flask, render_template, request, jsonify
from game_logic import get_computer_choice, determine_winner, get_score, check_final_winner, set_target, reset_game

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_target', methods=['POST'])
def set_target_score():
    data = request.get_json()
    target = int(data['target'])
    set_target(target)
    return jsonify({"message": "Target score set!", "target": target})

@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    user_choice = data['choice']
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    current_score = get_score()
    final_winner = check_final_winner()
    return jsonify({
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result,
        "score": current_score,
        "final_winner": final_winner
    })

@app.route('/reset', methods=['POST'])
def reset():
    reset_game()
    return jsonify({"message": "Game reset!"})

if __name__ == "__main__":
    app.run(debug=True, port=5004)
