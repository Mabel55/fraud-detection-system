from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # 1. Get the data from the HTML form
        amount = request.form['amount']
        location = request.form['location']
        
        # 2. Print it to the Terminal
        print(f"💰 New Transaction Received: ${amount} from {location}")
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)