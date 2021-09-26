from pycoingecko import CoinGeckoAPI
def coinpull():
    cg = CoinGeckoAPI()
    a = int(input())
    dat = cg.get_coins_markets( vs_currency="usd", per_page=a)
    for i in range(a):
        print(dat[i].get('name'))