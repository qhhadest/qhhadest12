import urllib.request
from html.parser import HTMLParser


class CoinMarketCapParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_span = False
        self.coins = []
        self.coin_list = [
            "Bitcoin",
            "Ethereum",
            "Binance Coin",
            "Tether",
            "Solana",
            "Cardano",
            "XRP",
            "Polkadot",
            "Dogecoin",
            "USD Coin",
            "Avalanche",
            "Litecoin",
            "Chainlink",
            "Stellar",
            "Polygon",
            "Tron",
            "Monero",
            "Uniswap",
            "Cosmos",
            "Shiba Inu"
        ]

    def handle_starttag(self, tag, attrs):
        if tag == 'span':
            self.in_span = True

    def handle_endtag(self, tag):
        if tag == 'span':
            self.in_span = False

    def handle_data(self, data):
        if self.in_span and data.startswith('$') and data[1].isdigit():
            self.coins.append(data)


url = "https://coinmarketcap.com/"
response = urllib.request.urlopen(url)
web_content = response.read().decode('utf-8')

parser = CoinMarketCapParser()
parser.feed(web_content)

print(parser.coins)
