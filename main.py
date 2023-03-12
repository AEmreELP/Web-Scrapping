import requests
import bs4
import pandas as pd

url = "https://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR=2013&MONTH=02&FROM=0100&TO=2812&STNM=17030"
result = requests.get(url,verify=False)

soup = bs4.BeautifulSoup(result.text,'lxml')
cases = []
cases = soup.find_all('pre')
for i in range(0,len(cases)):
    if(i%2==1):
        print(cases[i])

