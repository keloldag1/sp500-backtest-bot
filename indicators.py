import pandas as pd
import numpy as np

def calculate_indicators(df):
    df['SMA_5'] = df['close'].rolling(5).mean()
    df['SMA_20'] = df['close'].rolling(20).mean()

    delta = df['close'].diff()
    gain = delta.clip(lower=0).rolling(14).mean()
    loss = -delta.clip(upper=0).rolling(14).mean()
    rs = gain / (loss.replace(0, 1e-9))
    df['RSI'] = 100 - (100 / (1 + rs))

    return df.dropna().copy()
