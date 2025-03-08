from flask import Flask, request, jsonify
import sqlite3
import pickle
import numpy as np

app = Flask(__name__)

# Load ML Model
model = pickle.load(open("models/ml_model.pkl", "rb"))

# Database Connection
def get_db_connection():
    conn = sqlite3.connect('database/fitness_tracker.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['features']
    prediction = model.predict([np.array(data)])
    return jsonify({'prediction': prediction.tolist()})

@app.route('/user/<int:user_id>/progress', methods=['GET'])
def get_user_progress(user_id):
    conn = get_db_connection()
    progress = conn.execute('SELECT * FROM fitness_data WHERE user_id = ?', (user_id,)).fetchall()
    conn.close()
    return jsonify([dict(row) for row in progress])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
