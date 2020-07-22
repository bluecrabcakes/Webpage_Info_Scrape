from bs4 import BeautifulSoup
import requests


def scrape():
    webpage = input('>: ')
    source = requests.get(webpage).text
    soup = BeautifulSoup(source, 'lxml')
    name = soup.find('h3').text
    mobile = soup.find(id="ContentPlaceHolder1_DataList3_Label9_0").text
    email = soup.find(id="ContentPlaceHolder1_DataList3_Label10_0").text
    print(name)
    print(mobile)
    print(email)


scrape()