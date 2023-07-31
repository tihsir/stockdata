import bs4 as bs4
from bs4 import BeautifulSoup
import requests as requests
import json


def GetStockData(symbol):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/114.0.0.0 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{symbol}'
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    price = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text
    change = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text
    percent_change = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text
    print("Price (at close of Market):", price)
    print("Change:", change, percent_change)

def SearchStockSymbol(text):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/114.0.0.0 Safari/537.36'}
    url = 'https://google.com/search?q=what+is+the+stock+symbol+of+' + text
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    symbol = soup.find('div', {'class':'iAIpCb PZPZlf'}).find_all('span')[0].text
    return symbol[symbol.index(':') + 2:]

entry = input("Enter a stock you want to find data about:")
symbol = SearchStockSymbol(entry)
#print(symbol)
GetStockData(symbol)
