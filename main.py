from data import get_sp500_symbols, download_data
from indicators import calculate_indicators
from strategy import generate_signals
from backtest import backtest_signals
import analyze_results 


def run_backtest():
    symbols = get_sp500_symbols()
    results = []

    for symbol in symbols:
        print(f"Processing {symbol}...")
        df = download_data(symbol)
        if df is None or len(df) < 30:
            continue
        df = calculate_indicators(df)
        df = generate_signals(df)
        trades = backtest_signals(df)
        if not trades.empty:
            result = analyze_results(symbol, trades)
            results.append(result)

    analyze_results.display_top_results(results)

if __name__ == '__main__':
    run_backtest()
