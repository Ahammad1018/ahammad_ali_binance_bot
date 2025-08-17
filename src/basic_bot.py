from binance.client import Client

class BasicBot:
    def __init__(self, api_key: str, api_secret: str, testnet: bool = True):
        self.api_key = api_key
        self.api_secret = api_secret
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.FUTURES_BASE_URL = "https://testnet.binancefuture.com"

    def get_client(self):
        return self.client
