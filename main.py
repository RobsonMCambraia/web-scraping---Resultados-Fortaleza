import pandas as pd
import math
from bs4 import BeautifulSoup as bs
import requests
import re

url = "https://fortaleza1918.com.br/calendario/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
site = requests.get(url, headers=headers)
soup = bs(site.content, 'html.parser')

#Pega a data
results_mes = soup.find_all('div', class_='ctnLeft')
for result_mes in results_mes:
    data_tag = result_mes.find('p', class_='data')
    if data_tag:
        dia, mes = data_tag.get_text().split('/')
        # print(dia, mes)
        
#Time de casa
results_time1 = soup.find_all('div', class_='ctnCenter')
for result_time1 in results_time1:
    results_time_casa = result_time1.find_all('div', class_='timeCasa')
    for result_time_casa in results_time_casa:
        time_tag = result_time_casa.find('span', class_='nome')
        if time_tag:
            time_casa = time_tag.get_text()
            # print(time_casa)

#Time visitante
# .ctnCenter .timeVisita .nome
results_time2 = soup.find_all('div', class_='ctnCenter')
for result_time2 in results_time2:
    results_time_visitante = result_time2.find_all('div', class_='timeVisita')
    for result_time_visitante in results_time_visitante:
        time_visitante_tag = result_time_visitante.find('span', class_='nome')
        if time_visitante_tag:
            time_visitante = time_visitante_tag.get_text()
            print(time_visitante)