import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    sns.set_theme(style="whitegrid")
    
    # Configurations
    tickers = ['AAPL', 'MSFT', 'GOOGL']
    weights = [0.4, 0.3, 0.3]
    benchmark_ticker = '^GSPC'
    start_date = '2020-01-01'
    end_date = '2023-12-31'
    rf_rate = 0.02
    trading_days = 252

    print("Downloading historical data...")
    raw_data = yf.download(tickers, start=start_date, end=end_date)
    data = raw_data['Adj Close'] if 'Adj Close' in raw_data.columns else raw_data['Close']
    
    raw_bench = yf.download(benchmark_ticker, start=start_date, end=end_date)
    benchmark_data = raw_bench['Adj Close'] if 'Adj Close' in raw_bench.columns else raw_bench['Close']
    
    data = data.ffill().bfill()
    benchmark_data = benchmark_data.ffill().bfill()
    
    # Calculations
    returns = data.pct_change().dropna()
    benchmark_returns = benchmark_data.pct_change().dropna()
    portfolio_returns = returns.dot(weights)
    
    cum_portfolio = (1 + portfolio_returns).cumprod() - 1
    cum_benchmark = (1 + benchmark_returns).cumprod() - 1
    
    # Metrics
    portfolio_cum_return = cum_portfolio.iloc[-1]
    portfolio_ann_vol = portfolio_returns.std() * np.sqrt(trading_days)
    portfolio_ann_return = portfolio_returns.mean() * trading_days
    portfolio_sharpe = (portfolio_ann_return - rf_rate) / portfolio_ann_vol
    
    def calc_mdd(ret):
        cum = (1 + ret).cumprod()
        return ((cum - cum.cummax()) / cum.cummax()).min()
        
    portfolio_max_dd = calc_mdd(portfolio_returns)
    
    print("
--- Portfolio Metrics ---")
    print(f"Cumulative Return: {portfolio_cum_return:.2%}")
    print(f"Annualized Return: {portfolio_ann_return:.2%}")
    print(f"Annualized Volatility: {portfolio_ann_vol:.2%}")
    print(f"Sharpe Ratio: {portfolio_sharpe:.2f}")
    print(f"Max Drawdown: {portfolio_max_dd:.2%}")

if __name__ == '__main__':
    main()
