from flask import Flask, request, session, render_template, jsonify, redirect, url_for
from constants import APP_SECRET
import random

app = Flask(__name__)

app.debug = True
app.secret_key = APP_SECRET

@app.route('/')
@app.route('/index')
def index():
    if session.get('account_number'):
        data = {
            'account_number': session['account_number'],
            'formated_account_number': session['formated_account_number']
        }
        return render_template('index.html', data=data)
    else:
        data = {'signed_in': False}
        return render_template('index.html', data=data)
    
@app.route('/dashboard')
def dashboard():
    if session.get('account_number'):
        data = {
            'account_number': session['account_number'],
            'formated_account_number': session['formated_account_number']
        }
        return render_template('dashboard.html', data=data)
    else:
        return redirect(url_for('index'))

@app.route('/create')
def signup():

    digits = [str(random.randint(0, 9)) for _ in range(16)]
    number = "".join(digits)
    formatted_number = "-".join(number[i:i+4] for i in range(0, len(number), 4))

    session['account_number'] = number
    session['formated_account_number'] = formatted_number

    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()