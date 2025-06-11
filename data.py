import pandas as pd
import yfinance as yf
import sys
import os


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

        # Flatten multi-level columns, if any
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df.columns = df.columns.str.lower()  # 🔁 normalize to lowercase
        print(f"{symbol} columns: {df.columns.tolist()}")  # 🔍 optional debug

        df = df.dropna()
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None
