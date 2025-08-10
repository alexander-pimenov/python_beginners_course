import requests


# установка дополнительных пакетов осуществляется через пайтоновский установщик пакет pip

# функция get принимает на вход: "def get(url, params=None, **kwargs)"
symbol_btcusdt = {'symbol': 'BTCUSDT'}

response = requests.get('https://api.binance.com/api/v3/ticker/price', params=symbol_btcusdt)
content = response.content
print(content)
print(type(content))
price_object = response.json()
print(price_object)
print(type(price_object)) #{'symbol': 'BTCUSDT', 'price': '114033.35000000'}
price = float(price_object['price'])

import time

bitcoin_prices = []
for i in range(30):
    response = requests.get('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})
    # https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT
    # {
    #   "symbol": "BTCUSDT",
    #   "price": "114060.00000000"
    # }
    price = float(response.json()["price"])
    price = round(price, 2)
    bitcoin_prices.append(price)
    time.sleep(1)

print(bitcoin_prices)
print(len(bitcoin_prices)) # 30
print(max(bitcoin_prices)) # 114076.74
print(min(bitcoin_prices)) # 114033.35
