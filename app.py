from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'af5064a3c2ab89f5efe88e3d11ac854d' 

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        current_weather = get_weather(city)
        forecast = get_forecast(city)
        return render_template('index.html', current_weather=current_weather, forecast=forecast)
    return render_template('index.html')


def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()


def get_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)