"""
    *** This is a simple code that crawls COVID-19 data ***
        Today the only data crawled is the infected and
        the dead.
"""

from bs4 import BeautifulSoup
import requests
import pyperclip


link = "https://news.google.com/covid19/map?hl=pt-BR&mid=%2Fm%2F012l8y&gl=BR&ceid=BR%3Apt-419"
page = requests.get(link)

soup = BeautifulSoup(page.text, 'html.parser')

num_infectadosDF = soup.find(class_="fNm5wd qs41qe").text
num_infectadosDF = num_infectadosDF.replace("Total de casos", "")
num_infectadosDF = num_infectadosDF.replace("Informados ontem:", "")
num_infectadosDF = num_infectadosDF.split()

num_mortosDF = soup.find(class_="fNm5wd ckqIZ").text
num_mortosDF = num_mortosDF.replace("Mortes", "")
num_mortosDF = num_mortosDF.replace("Informados ontem:", "")
num_mortosDF = num_mortosDF.split()

print(f'Número de infectados no DF: {num_infectadosDF[0]}   |   Informados ontem: {num_infectadosDF[1]}')
print(f'Mortos no DF: {num_mortosDF[0]}  |  Informados ontem: {num_mortosDF[1]}')
# pyperclip.copy(page.text)

