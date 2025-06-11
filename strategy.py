def generate_signals(df):
    df['buy_signal'] = (
        (df['SMA_5'] > df['SMA_8']) &
        (df['SMA_8'] > df['SMA_13']) &
        (df['RSI'] < 40) &
        (df['Williams_%R'] < -30) &
        (df['MAMA'] > df['FAMA'])
    )
    df['sell_signal'] = (
        (df['SMA_5'] < df['SMA_8']) |
        (df['RSI'] > 80) |
        (df['Williams_%R'] > -20) |
        (df['MAMA'] < df['FAMA'])
    )
    return df
