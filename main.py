from flask import Flask, render_template, request, jsonify
from src.python.weather import getWeather, getAirCondition

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/apis/weather", methods=["GET"])
def homework_get():
    parameter= "state"
    guName = request.args.get(parameter)

    weather = getWeather(guName)
    airCondition = getAirCondition(guName)

    if weather == -2 or airCondition == -2:
        return jsonify({"message": "extern weather api error"})

    elif weather == -1 or airCondition == -1:
        return jsonify({"message": "internal server error"})

    else:
        return jsonify(dict(weather, **airCondition))

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

