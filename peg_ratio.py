import yfinance as yf

def peg_ratio(ticker):
    """Returns the PEG ratio of a stock.
    The 'PEG ratio' (price/earnings to growth ratio) is a valuation metric
    for determining the relative trade-off between the price of a stock,
    the earnings generated per share (EPS), and the company's expected growth

    The Trailing P/E Ratio is calculated by dividing a company's
    current share price by its most recent reported earnings per share (EPS)."""
    stock_info = yf.Ticker(ticker).info
    pe_ratio = stock_info["trailingPE"]
    eptss_growth_rate = stock_info["earningsQuarterlyGrowth"]
    peg_ratio = stock_info["pegRatio"]
    print(f"PE: {pe_ratio}\nEPS Growth: {eps_growth_rate}")
    return peg_ratio

# Test PEGs against: https://www.nasdaq.com/market-activity/stocks/crox/price-earnings-peg-ratios
ticker = input("Enter the ticker symbol of the stock: ")
peg_ratio = peg_ratio(ticker)
print(f"{ticker} PEG ratio: {peg_ratio}")
