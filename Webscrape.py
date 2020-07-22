from bs4 import BeautifulSoup
import requests

source = requests.get("http://www.indianngos.org/ngos_detail.aspx?state=Delhi").text
soup = BeautifulSoup(source, 'lxml')


for link in soup.find_all('a', href=True):
    links = (link['href'])

    print(f'http://www.indianngos.org/{links}')


