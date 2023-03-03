
"""
Программа узнает курсы валют, долара и евро. А так же переводит рубли в валюту (доллар или евро)
"""


import requests
from pprint import pprint
import bs4
from datetime import datetime

url = 'https://myfin.by/bank/kursy_valjut_nbrb'

HEADERS = {'Accept': '*/*',
           'Connection': 'keep-alive',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, '
                         'like Gecko) Chrome/71.0.3578.80 Safari/537.36OPR/56.0.3051.104'}

req = requests.get(url, headers=HEADERS)
text = req.text
soup = bs4.BeautifulSoup(text, features="html.parser")

course = soup.find(id='content_container')
for i in course:
    course1 = [item for item in i]
    lst = course1[0]
    usd = lst.find(class_="currency-block__value")
    USD = usd.text
    print(f'{USD}, usd')

    eur = lst.find_all(class_="currency-block__value")
    EUR = eur[1].text
    print(f'{EUR}, eur')

def just_eur_usd():
    x = f'{USD}, курс доллара.'
    y = f'{EUR}, курс евро.'
    z = f'Дата запроса: {datetime.now()}'
    print(x, y)
    return z


def in_eur_usd():
    rub = float(input('Введите число в бел рублях: '))
    type = input('Выберите тип валюты в который хотите первести(USD or EUR): ').upper()
    if type == 'USD':
        res = rub / float(USD)
        return res
    elif type == 'EUR':
        res1 = rub / float(EUR)
        return res1


def in_rub():
    type = input('Выберите тип валюты в который хотите первести рубли(USD or EUR): ').upper()
    rub = float(input('Введите число в выбранной вами валюте: '))
    if type == 'USD':
        res = rub * float(USD)
        return res
    elif type == 'EUR':
        res1 = rub * float(EUR)
        return res1w


def main(rub, eur_usd, currency):
    while True:
        type = input('Во что хотите перевести(В рубли или В валюту) или просто посмотреть курсы валют: ').upper()
        if type == 'В РУБЛИ':
            print(in_rub())
        elif type == 'В ВАЛЮТУ':
            print(in_eur_usd())
        elif type == 'КУРСЫ':
            print(just_eur_usd())
        elif type == 'СТОП':
            print('Программа остановлена. Приятного вечера!!')
            break


main(in_rub, in_eur_usd, just_eur_usd)
