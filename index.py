from flask import Flask, request, session, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from constants import format
import random

app = Flask(__name__)
app.config.from_pyfile('constants.py')
db = SQLAlchemy(app)

class Account(db.Model):
    number = db.Column(db.Integer, nullable=False, primary_key=True)
    balance = db.Column(db.Integer)

    def __repr__(self):
        return f'<Account {self.number}>'

@app.route('/')
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
    
@app.route('/test')
def test():
    accounts = Account.query.all()
    data = {'signed_in': False, 'accounts': accounts}
    return render_template('test.html', data=data)
    
@app.route('/login', methods=('GET', 'POST'))
def login():
    data = {'signed_in': False, 'error': False}
    
    if request.method == 'POST':
        account_number = request.form['account_number']
        if Account.query.get(account_number) != None:
            session['account_number'] = account_number
            session['formated_account_number'] = format(account_number)

            return redirect(url_for('index'))
        else:

            return render_template('login.html', data={'signed_in': False, 'error': True})

    return render_template('login.html', data=data)

@app.route('/signup')
def signup():

    number = "".join([str(random.randint(0, 9)) for _ in range(16)])

    session['account_number'] = number
    session['formated_account_number'] = format(number)

    account = Account(number=number, balance=0)
    db.session.add(account)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()