import pandas as pd
import numpy as np

def calculate_mama(price, fastlimit=0.5, slowlimit=0.05):
    mama = np.zeros(len(price))
    fama = np.zeros(len(price))
    mama[0] = price.iloc[0]
    fama[0] = price.iloc[0]
    for i in range(1, len(price)):
        mama[i] = mama[i-1] + fastlimit * (price.iloc[i] - mama[i-1])
        fama[i] = fama[i-1] + slowlimit * (mama[i] - fama[i-1])
    return pd.Series(mama, index=price.index), pd.Series(fama, index=price.index)

def calculate_indicators(df):
    df['SMA_5'] = df['Close'].rolling(5).mean()
    df['SMA_8'] = df['Close'].rolling(8).mean()
    df['SMA_13'] = df['Close'].rolling(13).mean()
    df['EMA_5'] = df['Close'].ewm(span=5, adjust=False).mean()
    df['EMA_8'] = df['Close'].ewm(span=8, adjust=False).mean()
    df['EMA_13'] = df['Close'].ewm(span=13, adjust=False).mean()

    delta = df['Close'].diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = -delta.clip(upper=0).rolling(14).mean()
    rs = gain / (loss.replace(0, 1e-9))
    df['RSI'] = 100 - (100 / (1 + rs))

    mama, fama = calculate_mama(df['Close'])
    df['MAMA'] = mama
    df['FAMA'] = fama

    df['High_14'] = df['High'].rolling(14).max()
    df['Low_14'] = df['Low'].rolling(14).min()
    df['Williams_%R'] = (df['High_14'] - df['Close']) / (df['High_14'] - df['Low_14']) * -100

    return df.dropna()
