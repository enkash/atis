from flask import Flask
#import atis_india
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/<icao>')
def landing(icao):
	payload = { "username" : "nkashyap", "password":"supernova" , "submit":"Submit" }
	session_requests = requests.session()
	login_url = "http://www.acdm.in/index.php"
	result = session_requests.post(login_url, data=payload, headers = dict(referer=login_url))
	atis_url = "http://www.acdm.in/ShowStations.php"
	station = {"q":icao}
	result2 = session_requests.post(atis_url, data=station, headers = dict(referer=login_url))
	soup = BeautifulSoup(result2.text,'html.parser')
	tds = soup.findAll("td")
	atis_text = "<div style='white-space: pre-wrap'>"
	if len(tds)>0:
		atis_text += tds[1].string
		atis_text += "</div>"
		return atis_text
	return "%s ATIS NOT AVAILABLE" % icao.upper()


#@app.route('/getatis')
#def get_atis():
#	return 'atis of'