# app.py
# A Flask backend that returns detailed case data and logs it to SQLite.
# To run this:
# 1. Install Flask and Flask-CORS: pip install Flask flask-cors
# 2. Run the server from your terminal: python app.py

import sqlite3
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import time
import random

# --- Database Setup ---
DB_NAME = 'query_log.db'

def init_db():
    """Initializes the database and creates the 'logs' table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    # Create table to store query logs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS query_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            case_type TEXT NOT NULL,
            case_number TEXT NOT NULL,
            filing_year TEXT NOT NULL,
            response_data TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

# --- Flask App Initialization ---
app = Flask(__name__)
# Enable CORS (Cross-Origin Resource Sharing) to allow the frontend to make requests
CORS(app)

@app.route('/api/fetch-case', methods=['POST'])
def fetch_case_data():
    """
    API endpoint to receive case details, log them, and return a detailed response.
    """
    conn = None
    try:
        # 1. Get data from the frontend request
        data = request.get_json()
        case_type = data.get('caseType')
        case_number = data.get('caseNumber')
        filing_year = data.get('filingYear')

        print(f"Received request for: {case_type} - {case_number}/{filing_year}")

        # 2. Simulate web scraping delay
        time.sleep(1.5)

        # 3. Create detailed mock response data
        # This data structure matches what the frontend's populateResults function expects.
        mock_response_data = {
            "parties": f"State of India vs. Litigant for Case {case_number}",
            "filingDate": f"20-Feb-{filing_year}",
            "caseStatus": random.choice(["Pending", "Disposed"]),
            "presidingJudge": random.choice(["Hon'ble Justice R. Singh", "Hon'ble Justice P. Sharma", "Hon'ble Justice A. Gupta"]),
            "nextHearing": "05-Nov-2025",
            "pdfDate": "01-Aug-2024",
            "pdfUrl": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
        }

        # 4. Log the query and response to the SQLite database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO query_logs (case_type, case_number, filing_year, response_data) VALUES (?, ?, ?, ?)",
            (case_type, case_number, filing_year, json.dumps(mock_response_data)) # Store response as a JSON string
        )
        conn.commit()
        print(f"Successfully logged query for case {case_number}/{filing_year} to the database.")

        # 5. Return the data as JSON to the frontend
        return jsonify(mock_response_data)

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "An internal server error occurred"}), 500
    
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    # Initialize the database when the server starts
    init_db()
    # Run the app in debug mode on port 5000
    app.run(debug=True, port=5000)
