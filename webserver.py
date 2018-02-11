from flask import Flask, redirect, url_for, render_template, request
from quickstart import create_event

app = Flask(__name__)

@app.route('/login')
def welcome():
    return app.send_static_file('login.html')

@app.route('/setup')
def setup():
    return app.send_static_file('setup.html')

@app.route('/thankyou')
def thankyou():
    return app.send_static_file('thankyou.html')

@app.route('/home')
def home():
    return app.send_static_file('home.html')

@app.route('/notification')
def notification():
    return app.send_static_file('notification.html')

@app.route('/send-invite')
def sendInvite():
    create_event()
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return app.send_static_file('home.html')

@app.route('/alert')
def alert():
    return app.send_static_file('alert.html')

@app.route('/accept')
def accept():
    return app.send_static_file('accept.html')

app.run(host="0.0.0.0")
