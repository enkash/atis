from flask import Flask
import atis_india

app = Flask(__name__)

@app.route('/<icao>')
def landing(icao):
	return atis_india.get_atis(icao)

@app.route('/getatis')
def get_atis():
	return 'atis of'