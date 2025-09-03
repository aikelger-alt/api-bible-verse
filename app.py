from flask import Flask, jsonify, render_template
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# PULLED THIS SHIT

verses = [
    {"verse": "John 3:16", "text": "For God so loved the world that he gave his one and only Son."},
    {"verse": "Psalm 23:1", "text": "The Lord is my shepherd; I shall not want."},
    {"verse": "Philippians 4:13", "text": "I can do all things through Christ who strengthens me."},
    {"verse": "Romans 8:28", "text": "All things work together for good to those who love God."}
]

@app.route('/')
def home():
    return render_template('landingpage.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

# <-- This is the function you're asking about:
@app.route('/random-verse', methods=['GET'])
def get_random_verse():
    return jsonify(random.choice(verses))

if __name__ == '__main__':
    app.run(debug=True)
