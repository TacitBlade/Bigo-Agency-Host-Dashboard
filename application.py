import os
from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps
import pandas as pd
import requests

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key')  # Use environment variable for production

# Simulated user database (replace with AWS RDS later)
users = {
    'host1': {'password': 'pass123', 'role': 'Host'},
    'agency1': {'password': 'pass456', 'role': 'Agency'}
}

# Google Sheet configuration
SHEET_ID = '1lOEqHyPjZq6wEXL8oPEg3I6K-s5o9Au4-hNueiAizOU'  # Replace with your SHEET_ID
HOST_PAYMENTS_GID = '0258050291'  # GID for Host Payments
AGENCY_PAY_SHEET_ID = "1W5wHrqS3EZbXZUYVm8BKg0gjsL8RnKkew2eVd8SEnGQ"
AGENCY_PAY_SHEET_GID = '315628013'  # GID for Agency Pay Sheet tab

# Role-based access control decorator
def login_required(role=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'username' not in session:
                return redirect(url_for('login'))
            if role and session.get('role') != role:
                return redirect(url_for('dashboard'))
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# Fetch Google Sheet data
def fetch_sheet_data(sheet_id, gid):
    try:
        url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gid={gid}/export?format=csv"
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        return pd.read_csv(response.content).to_dict(orient='records')
    except Exception as e:
        print(f"Error fetching sheet data: {e}")
        return []

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            session['username'] = username
            session['role'] = users[username]['role']
            return redirect(url_for('dashboard'))
        return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/dashboard')
@login_required()
def dashboard():
    return render_template('dashboard.html', role=session['role'])

@app.route('/charts')
@login_required()
def charts():
    data = fetch_sheet_data(SHEET_ID, HOST_PAYMENTS_GID)
    return render_template('charts.html', data=data)

@app.route('/agency-pay-sheet')
@login_required(role='Agency')
def agency_pay_sheet():
    data = fetch_sheet_data(AGENCY_PAY_SHEET_ID, AGENCY_PAY_SHEET_GID)
    return render_template('charts.html', data=data)

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('role', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)