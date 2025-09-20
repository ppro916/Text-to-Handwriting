from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    word = request.form.get('word', '')
    size = request.form.get('size', 50)
    
    valid_chars = []
    
    for char in word:
        if char == ' ':
            valid_chars.append('SPACE')
        elif char in ".,!?;:'\"-()":
            punctuation_map = {
                '.': 'FULLSTOP',
                ',': 'COMMA', 
                '!': 'EXCLAMATION',
                '?': 'QUESTION',
                ';': 'SEMICOLON',
                ':': 'COLON',
                "'": 'APOSTROPHE',
                '"': 'QUOTATION',
                '-': 'HYPHEN',
                '(': 'PAREN_LEFT',
                ')': 'PAREN_RIGHT'
            }
            if char in punctuation_map:
                valid_chars.append(punctuation_map[char])
        elif char.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            img_path = f"static/letters/{char.upper()}.png"
            if os.path.exists(img_path):
                valid_chars.append(char.upper())
    
    return render_template('result.html', word=word, display_chars=valid_chars, size=size)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
