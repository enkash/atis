import requests
from bs4 import BeautifulSoup

payload = { "username" : "nkashyap", "password":"supernova" , "submit":"Submit" }
session_requests = requests.session()
login_url = "http://www.acdm.in/index.php"
result = session_requests.post(login_url, data=payload, headers = dict(referer=login_url))
atis_url = "http://www.acdm.in/ShowStations.php"
station = {"q":"VOHS"}
result = session_requests.post(atis_url, data=station, headers = dict(referer=login_url))
soup = BeautifulSoup(result.text)
print(soup.find_all('td')[1].string)

GIT Commands
On local machine, to push changes to github "https://github.com/enkash/atis.git"
git status
git commit #commit local changes
git push

On server machine, to get new changes
git pull

