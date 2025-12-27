from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import pickle
import csv

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Load AI
with open('fraud_model.pkl', 'rb') as file:
    model = pickle.load(file)

# --- LOGIN ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "admin" and password == "secure123":
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            error = "❌ Access Denied!"
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/forgot', methods=['GET', 'POST'])
def forgot():
    message = None
    error = None
    if request.method == 'POST':
        if request.form['pin'] == "9999":
            message = "secure123"
        else:
            error = "❌ Wrong Master PIN!"
    return render_template('forgot.html', password=message, error=error)

# --- MAIN APP ---
@app.route('/', methods=['GET', 'POST'])
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    result = "" 
    if request.method == 'POST':
        # Get Data
        trans_type = request.form['trans_type']  # <--- WE ADDED THIS
        amount = request.form['amount']
        location = request.form['location']
        account = request.form['account_type']
        time = request.form['time']

        # 1. CHECK FOR REVERSAL SCAM
        if trans_type == "Reversal":
            result = "⚠️ SCAM ALERT: FAKE REVERSAL DETECTED!"
            with open('fraud_log.csv', 'a', newline='') as file:
                csv.writer(file).writerow([amount, location, "REVERSAL_SCAM", time, "BLOCKED"])
        
        # 2. IF NORMAL, ASK THE AI
        else:
            loc_code = {'Lagos': 0, 'Abuja': 1, 'Kano': 2, 'Ibadan': 3, 'Russia': 4, 'China': 5, 'USA': 6, 'Forest': 7, 'Remote': 8}.get(location, 0)
            acc_code = {'Student': 0, 'Corporate': 1}.get(account, 0)

            pred = model.predict([[float(amount), loc_code, acc_code, int(time)]])
            
            if pred[0] == 1:
                result = "⚠️ FRAUD DETECTED!"
                with open('fraud_log.csv', 'a', newline='') as file:
                    csv.writer(file).writerow([amount, location, account, time, "BLOCKED"])
            else:
                result = "✅ Transaction Safe"

    return render_template('index.html', prediction_text=result)

# --- NEW: ADMIN DASHBOARD ---
@app.route('/database')
def database():
    # Check if user is logged in
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    # Read the CSV file
    transactions = []
    try:
        with open('fraud_log.csv', 'r') as file:
            reader = csv.reader(file)
            transactions = list(reader)
    except FileNotFoundError:
        pass # It's okay if file doesn't exist yet

    return render_template('dashboard.html', transactions=transactions)

if __name__ == '__main__':
    app.run(debug=True)