from bs4 import BeautifulSoup
import requests
import openpyxl as xl

wb = xl.load_workbook("Book3.xlsx")
sheet = wb['Sheet1']


def scrape():
    while True:
        webpage = sheet['A2'].value
        source = requests.get(webpage + ' ').text
        if webpage != 'exit':
            soup = BeautifulSoup(source, 'lxml')
            name = soup.find('h3').text
            mobile = soup.find(id="ContentPlaceHolder1_DataList3_Label9_0").text
            phone = soup.find(id="ContentPlaceHolder1_DataList3_Label8_0").text
            email = soup.find(id="ContentPlaceHolder1_DataList3_Label10_0").text
            website = soup.find(id="ContentPlaceHolder1_DataList3_Label11_0").text
            print(f'Name: {name}')
            print(f'Mobile: {mobile}')
            print(f'Phone: {phone}')
            print(f'Email: {email}')
            print(f'Website: {website}')
            print()
            continue


scrape()
