import requests
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['DEBUG']=True

@app.route('/')
def index():
    url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=8625b46b1df662e9223ab2fa4771e56f'
    city='Las Vegas'
    r=requests.get(url.format(city)).json()
    print(r)
    return render_template('weather.html')