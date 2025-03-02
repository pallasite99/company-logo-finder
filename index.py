from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import sqlite3
import time

app = Flask(__name__)
CORS(app)

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect("logos.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS company_logos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT UNIQUE,
            domain TEXT,
            logo_url TEXT
        )
    """)
    conn.commit()
    conn.close()

# Fetch company list from a dataset (example API or file needed)
def get_large_company_list():
    # This should be replaced with an actual dataset containing 50,000 companies
    return [
        "Google", "Microsoft", "Amazon", "Facebook", "Apple",
        "Tesla", "Netflix", "Adobe", "Intel", "Cisco"
    ] * 5000  # Replicating to simulate 50,000 entries

# Fetch and store company logos dynamically
def populate_database():
    conn = sqlite3.connect("logos.db")
    cursor = conn.cursor()
    
    company_list = get_large_company_list()
    for company in company_list:
        domain = company.lower().replace(' ', '').replace(',', '').replace('&', 'and') + ".com"
        logo_url = f"https://logo.clearbit.com/{domain}"
        
        try:
            cursor.execute("INSERT INTO company_logos (company_name, domain, logo_url) VALUES (?, ?, ?)",
                           (company, domain, logo_url))
        except sqlite3.IntegrityError:
            pass  # Ignore duplicates
    
    conn.commit()
    conn.close()

@app.route('/get_logos', methods=['POST'])
def get_logos():
    data = request.json
    company_names = data.get("companies", [])
    
    conn = sqlite3.connect("logos.db")
    cursor = conn.cursor()
    result = {}
    
    for company in company_names:
        cursor.execute("SELECT logo_url FROM company_logos WHERE company_name = ?", (company,))
        row = cursor.fetchone()
        if row:
            result[company] = row[0]
        else:
            # If not found, generate a Clearbit URL dynamically
            domain = company.lower().replace(' ', '').replace(',', '').replace('&', 'and') + ".com"
            result[company] = f"https://logo.clearbit.com/{domain}"
    
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    init_db()
    populate_database()
    app.run(debug=True)
