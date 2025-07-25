from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import os
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')

# Sample data for dashboard (replace with actual data source)
sample_host_data = {
    'total_hosts': 150,
    'active_hosts': 128,
    'top_performers': [
        {'name': 'Host A', 'revenue': 5000, 'viewers': 1200},
        {'name': 'Host B', 'revenue': 4500, 'viewers': 980},
        {'name': 'Host C', 'revenue': 3800, 'viewers': 850}
    ],
    'monthly_revenue': 125000,
    'total_viewers': 45000
}

@app.route('/')
def index():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', data=sample_host_data)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Simple authentication (replace with proper authentication)
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            session['username'] = username
            flash('Successfully logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials!', 'error')
    
    return render_template('login.html')

@app.route('/charts')
def charts():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    return render_template('charts.html', data=sample_host_data)

@app.route('/api/chart-data')
def chart_data():
    if 'logged_in' not in session:
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Sample chart data
    chart_data = {
        'revenue_trend': {
            'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'data': [80000, 95000, 110000, 105000, 120000, 125000]
        },
        'host_performance': {
            'labels': [host['name'] for host in sample_host_data['top_performers']],
            'data': [host['revenue'] for host in sample_host_data['top_performers']]
        }
    }
    return jsonify(chart_data)

@app.route('/logout')
def logout():
    session.clear()
    flash('Successfully logged out!', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
