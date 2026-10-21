# Portfolio Performance & Risk Evaluator

An interactive financial application developed in Python to evaluate the performance and risk of an investment portfolio against a market benchmark (S&P 500).

## Features
- Custom asset allocation for at least three stocks or ETFs.
- Computes essential portfolio metrics: Annualized Return, Annualized Volatility, Sharpe Ratio, and Maximum Drawdown.
- Benchmarks portfolio performance against the S&P 500 index (`^GSPC`).
- Generates clean, interactive allocation pie charts and cumulative return comparisons.

## Financial Concepts & Calculations
- **Annualized Return**: Compounds the mean daily returns scaled to 252 annual trading days.
- **Annualized Volatility**: Measures price fluctuations via the standard deviation of daily returns, annualized using the square-root of time rule (`std * sqrt(252)`).
- **Sharpe Ratio**: Evaluates risk-adjusted performance using an assumed risk-free rate of 2% (`(portfolio_return - RF) / volatility`).
- **Maximum Drawdown**: Measures the worst peak-to-trough drop in portfolio value over the specified timeline.

## Quick Start
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python portfolio_app.py
   ```

## Datasets & APIs Used
- **Yahoo Finance API (yfinance)**: Used to retrieve real-time and historical daily adjusted close price data.

## AI Agent Explanation
This application was engineered with the assistance of a Colab AI assistant. The AI helped debug the `yfinance` multi-indexing API updates, optimize vector matrix calculations for the weighted portfolio return, and structure risk metric scripts accurately.

## Limitations & Future Extensions
- Uses a fixed, assumed risk-free rate of 2.0% (could pull dynamic Treasury bill yields).
- Assumes static portfolio weights without periodic rebalancing.
- The purpose of the application 
