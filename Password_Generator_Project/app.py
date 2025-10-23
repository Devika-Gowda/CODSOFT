from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

# Password generation function
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        length = int(request.form['length'])
        if length <= 0:
            return jsonify({'error': 'Enter a positive number!'})
        password = generate_password(length)
        return jsonify({'password': password})
    except ValueError:
        return jsonify({'error': 'Please enter a valid number!'})

if __name__ == '__main__':
    app.run(debug=True)
