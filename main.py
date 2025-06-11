import pandas as pd
import json

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

    # ✅ Print to console
    results_df = pd.DataFrame(results)
    results_df.sort_values(by='sharpe_ratio', ascending=False, inplace=True)
    print("\nTop Performing Symbols:")
    print(results_df.head(10))

    # ✅ Save to CSV
    results_df.to_csv("results.csv", index=False)

    # ✅ Optional: Save full JSON version
    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

if __name__ == '__main__':
    run_backtest()
