import requests
from bs4 import BeautifulSoup

siteDate = requests.get('https://ru.investing.com/currencies/usd-uah')

print(siteDate.status_code)

siteSoup = BeautifulSoup(siteDate.text, features='html.parser')

rates = siteSoup.find_all(name='div', attrs={'class': 'text-5xl/9'})

for rate in rates:
    print('Dollar exchange rate: ',rate.text)

hryvnias = input(str('Enter the amount of hryvnias: '))
USADollar = 39.9481
try:
    Conversion = float(hryvnias)/float(USADollar)

    print(round(Conversion, 3))
except ValueError:
    print(ValueError)

