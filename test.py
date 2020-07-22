from bs4 import BeautifulSoup
import requests
import openpyxl as xl

wb = xl.load_workbook("Book3.xlsx")
sheet = wb['Sheet1']
outputwb = xl.load_workbook('Book4.xlsx')
outputsheet = outputwb['Sheet1']


source = requests.get(sheet['A2'].value).text

soup = BeautifulSoup(source, 'lxml')

name = soup.find('h3').text
mobile = soup.find(id="ContentPlaceHolder1_DataList3_Label9_0").text
phone = soup.find(id="ContentPlaceHolder1_DataList3_Label8_0").text
email = soup.find(id="ContentPlaceHolder1_DataList3_Label10_0").text
website = soup.find(id="ContentPlaceHolder1_DataList3_Label11_0").text

outputsheet['A2'] = name
outputsheet['B2'] = mobile + phone
outputsheet['C2'] = email
outputsheet['D2'] = website

outputwb.save("Book4.xlsx")




