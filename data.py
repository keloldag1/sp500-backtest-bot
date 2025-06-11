import pandas as pd
import yfinance as yf

def get_sp500_symbols():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    tables = pd.read_html(url)
    df = tables[0]
    return [symbol.replace('.', '-') for symbol in df['Symbol'].tolist()]

def download_data(symbol, period='3mo', interval='1d'):
    try:
        df = yf.download(symbol, period=period, interval=interval, progress=False)
        if df.empty:
            return None
        return df.dropna()
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None
