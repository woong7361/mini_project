from flask import Flask, render_template, request, jsonify
from weather import getWeather, getAirCondition

app = Flask(__name__)


@app.route("/homework", methods=["GET"])
def homework_get():
    parameter= "state"
    guName = request.form[parameter]

    weather = getWeather(guName)
    airCondition = getAirCondition(guName)

    if weather == -1 or airCondition == -1:
        return jsonify()

    return jsonify(dict(weather, **airCondition))

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

