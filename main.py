from flask import Flask, render_template
from jinja2 import Template, FileSystemLoader, Environment
from pyowm import OWM
from pyowm.utils.config import get_default_config
from key import key

owm = OWM(key)
config_dict = get_default_config()
config_dict["language"] = 'ru'
place = "Белгород"
manager = owm.weather_manager()
observation = manager.weather_at_place(place)
weather = observation.weather
temp_ = weather.temperature("celsius")

app = Flask(__name__)
loader = FileSystemLoader("templates")
env = Environment(loader=loader)
test = weather.detailed_status

@app.route('/')
def index():
    tm = env.get_template("index.htm")
    return render_template('index.htm')


@app.route("/weather")
def weather():
    tm = env.get_template("weather.htm")
    return render_template('weather.htm', title="Погода", temperature=temp_["temp"], fells_like=temp_["feels_like"],
                           mark=test)


if __name__ == "__main__":
    app.run(debug=True)
