from flask import Flask, redirect, url_for, render_template, request
from quickstart import create_event

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return app.send_static_file('welcome.html')

@app.route('/send-invite')
def sendInvite():
    create_event()
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return 'this works!'

app.run(host="0.0.0.0")
