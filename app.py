from flask import Flask, redirect, url_for, render_template, request, jsonify, session
from pymongo import MongoClient
import requests
from datetime import datetime
from bson import ObjectId

app = Flask(__name__)
app.secret_key = "your_secret_key"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('aboutus.html')

@app.route('/social')
def social():
    return render_template('Social Contribution.html')
    
@app.route('/our')
def our():
    return render_template('OurPartners.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Dummy user validation
        if username == 'admin' and password == 'admin':
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/24hours')
def hours():
    return render_template('24hours.html')

@app.route('/scada')
def scada():
    return render_template('scada.html')

@app.route('/advanced')
def advanced():
    return render_template('advanced.html')

@app.route('/environment')
def environment():
    return render_template('environment.html')

@app.route('/fasttrans')
def fasttrans():
    return render_template('fasttrans.html')

@app.route('/constructive')
def cons():
    return render_template('constructive.html')
    

if __name__=='__main__':
    app.run('0.0.0.0',port=5000, debug=True)