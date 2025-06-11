import numpy as np
import pandas as pd

def backtest_signals(df):
    position = False
    entry_price = 0
    returns = []

    for i in range(1, len(df)):
        if df['buy_signal'].iloc[i] and not position:
            entry_price = df['close'].iloc[i]
            position = True
        elif df['sell_signal'].iloc[i] and position:
            exit_price = df['close'].iloc[i]
            returns.append((exit_price - entry_price) / entry_price)
            position = False

    if position:
        returns.append((df['close'].iloc[-1] - entry_price) / entry_price)

    return pd.Series(returns)

def analyze_results(symbol, trades):
    cumulative_return = (1 + trades).prod() - 1
    avg_return = trades.mean()
    std_dev = trades.std()
    sharpe = avg_return / std_dev * np.sqrt(252) if std_dev > 0 else 0
    win_rate = (trades > 0).mean()
    max_drawdown = (1 + trades.cumsum()).cummax() - (1 + trades.cumsum())
    drawdown = max_drawdown.max()

    return {
        'symbol': symbol,
        'total_trades': len(trades),
        'win_rate': round(win_rate, 2),
        'cumulative_return': round(cumulative_return, 2),
        'sharpe_ratio': round(sharpe, 2),
        'max_drawdown': round(drawdown, 2)
    }

def display_top_results(results):
    results_df = pd.DataFrame(results)
    results_df.sort_values(by='sharpe_ratio', ascending=False, inplace=True)
    print("\nTop Performing Symbols:")
    print(results_df.head(10))
