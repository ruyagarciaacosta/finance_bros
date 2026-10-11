import pandas as pd
import yfinance as fy

class ticker_data():

    def __init__(self, ticker_name):
        self.ticker_name = ticker_name
        self.set_ticker = fy.Ticker(str(self.ticker_name))
        self.ticker_data = self.set_ticker.info()
        pass

    def get_current_price( self ):
        self.set_ticker.curre
        if self.current_price:
            print(self.current_price)
        else: 
            print('Get a Ticker first then continue.')
        return
    
if __name__ == "__main__":
    intel = ticker_data('INTC')
    print(intel.ticker_data )