import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('weather.html')