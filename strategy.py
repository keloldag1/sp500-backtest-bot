def generate_signals(df):
    df['buy_signal'] = (df['SMA_5'] > df['SMA_20']) & (df['RSI'] < 30)
    df['sell_signal'] = (df['SMA_5'] < df['SMA_20']) & (df['RSI'] > 70)
    return df