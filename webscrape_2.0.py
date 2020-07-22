from bs4 import BeautifulSoup
import requests
import csv

source = requests.get("http://www.indianngos.org/ngos_detail.aspx?state=Delhi").text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('ngo_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Links'])

for link in soup.find_all('a', href=True):
    links = (link['href'])

    output = f'http://www.indianngos.org/{links}'

    print()

    csv_writer.writerow([output])

csv_file.close()
