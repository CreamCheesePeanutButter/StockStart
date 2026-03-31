from const.const import API_KEY, STOCK_HISTORY_API_KEY
import requests

class Stock:
    current_price = 0
    high_today = 0
    low_today = 0
    open_price = 0
    previous_close = 0
    _ticker = ""
    name = ""
    currency = "USD"
    _history = {"close": [], "open": []}
    
    def __init__(self, ticker):
        self._ticker = ticker
        self.update()


    def update_name(self):
        url = f"https://finnhub.io/api/v1/stock/profile2?symbol={self._ticker}&token={API_KEY}"
        response = requests.get(url)
        data = response.json()
        self.name = data.get("name", self._ticker)

    # get stock history
    # type here is the stock history in months or in years (MONTH, YEAR)
    # for now the type is not exist yet
    def get_stock_history(self):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={self._ticker}&apikey={STOCK_HISTORY_API_KEY}'
        r = requests.get(url)
        data = r.json()
        _history = data.get("Monthly Time Series", {})
        years = _history.keys()
        close_stock_values = []
        open_stock_values = []

        for year in years:
            close_stock_values.append(_history[year]['4. close'])
            open_stock_values.append(_history[year]['1. open'])

        self._history["close"] = close_stock_values
        self._history["open"] = open_stock_values

    def update(self):
        url = f"https://finnhub.io/api/v1/quote?symbol={self._ticker}&token={API_KEY}"
        response = requests.get(url)
        data = response.json()
        self.current_price = data["c"]
        self.high_today = data["h"]
        self.low_today = data["l"]
        self.open_price = data["o"]
        self.previous_close = data["pc"]
        self.update_name()
        if self.currency != "USD":
            self.exchange_to_currency()
        else:
            self.currency = "USD"
        self.get_stock_history()



class StockTracker:
    _stocks = {}
    _currency = "USD"
    def __init__(self):
        self._stocks = {
            "AAPL": Stock("AAPL"),
            "GOOGL": Stock("GOOGL"),
            "AMZN": Stock("AMZN")
        }
        self._currency = "USD"
    
    def get_currency(self):
        return self._currency
    
    def get_stocks(self):
        return self._stocks

    def add_stock(self, ticker):
        if ticker not in self._stocks:
            self._stocks[ticker] = Stock(ticker)

    def update_all(self):
        for stock in self._stocks.values():
            stock.update()

    def exchange_currency(self, currency):
        url = f"https://open.er-api.com/v6/latest/{self._currency}"
        data = requests.get(url).json()
        rate = data["rates"][currency]

        for stock in self._stocks.values():
            stock.current_price *= rate
            stock.high_today *= rate
            stock.low_today *= rate
            stock.open_price *= rate
            stock.previous_close *= rate
            stock.currency = currency

        self._currency = currency
    def get_stock_history(self, ticker):
        if ticker in self._stocks:
            return self._stocks[ticker]._history
        else:
            return None
    


            

        
