import requests
from bs4 import BeautifulSoup

def get_atis(icao):
	payload = { "username" : "nkashyap", "password":"supernova" , "submit":"Submit" }
	session_requests = requests.session()
	login_url = "http://www.acdm.in/index.php"
	result = session_requests.post(login_url, data=payload, headers = dict(referer=login_url))
	atis_url = "http://www.acdm.in/ShowStations.php"
	station = {"q":icao}
	result2 = session_requests.post(atis_url, data=station, headers = dict(referer=login_url))
	soup = BeautifulSoup(result2.text,'html.parser')
	atis_text = (soup.find_all("td")[1].string)
	#print("length of atis_text = ",len(soup.find_all('td')[1]))
	#print("I'm here")
	return str(atis_text)
	