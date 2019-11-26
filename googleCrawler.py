from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

baseUrl ='https://www.google.com/search?q='
plusUrl = input('무엇을 검색할까요? : ')
url = baseUrl + quote_plus(plusUrl)

driver = webdriver.Chrome()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html)

r = soup.select('.rc')

searchList=[]

for i in r:
    temp =[]
    temp.append(i.text)
    temp.append(i.a.attrs['href'])
    searchList.append(temp)
 #   print(i.select_one('.S3Uucc').text)
  #  print(i.select_one('.iUh30').text)
   # print(i.a.attrs['href'])
    #print()

f=open(f'{plusUrl}.csv','w',encoding='utf-8',newline='')
csvWriter = csv.writer(f)
for i in searchList:
    csvWriter.writerow(i)

f.close()

print('Complete!!')

driver.close()