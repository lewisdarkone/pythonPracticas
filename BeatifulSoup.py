import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.ciudadredonda.org/calendario-lecturas/evangelio-del-dia/?f=2019-07-06')
soup = BeautifulSoup(req.text,"lxml")

print(soup.title)
print(soup.title.name)
print(soup.title.string)

for bHead in soup.find_all('b'):
    print(bHead.text)