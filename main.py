import bs4
import requests
import csv

for year in range(13,23):
    if(year%4==0):
        day=29
    else:
        day=28
    url = "https://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR=20"+str(year)+"&MONTH=02&FROM=0100&TO="+str(day)+"12&STNM=17030"
    result = requests.get(url,verify=False)

    soup = bs4.BeautifulSoup(result.text,'lxml')
    cases = []
    cases = soup.find_all('pre')

    file = open('subatLast.csv','a')
    file = csv.writer(file)

    for i in range(0,len(cases)):
        if(i%2==1):
            k = cases[i].text.replace('\n','""')
            print(k)
            file.writerow([k])






