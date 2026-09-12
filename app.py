from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(name)
CORS(app)  # هذا السطر مهم جداً حتى يسمح لموقعك على Netlify يسحب البيانات بدون مشاكل حظر

@app.route('/')
def home():
    return "Vodu Bridge API is Running Successfully!"

@app.route('/api/movies', methods=['GET'])
def get_movies():
    try:
        filename = 'movies.json'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return jsonify(data)
        else:
            return jsonify({"status": "error", "message": "Database file not found."}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)