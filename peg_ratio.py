import pprint
import yfinance as yf


def peg_ratio(ticker):
    """Returns the PEG ratio of a stock.
    The 'PEG ratio' (price/earnings to growth ratio) is a valuation metric
    for determining the relative trade-off between the price of a stock,
    the earnings generated per share (EPS), and the company's expected growth

    The Trailing P/E Ratio is calculated by dividing a company's
    current share price by its most recent reported earnings per share (EPS)."""
    stock_info = yf.Ticker(ticker).info
    pprint.pprint(stock_info)
    # pe_ratio = stock_info["trailingPE"]
    # eps_growth_rate = stock_info["earningsQuarterlyGrowth"]
    # peg_ratio = pe_ratio / eps_growth_rate
    # print(f"PE: {pe_ratio}\nEPS Growth: {eps_growth_rate}")
    peg_ratio = stock_info["pegRatio"]
    trailing_peg_ratio = stock_info["trailingPegRatio"]
    company_name = stock_info["shortName"]
    return peg_ratio, trailing_peg_ratio, company_name


# Test PEGs against: https://www.nasdaq.com/market-activity/stocks/crox/price-earnings-peg-ratios
ticker = input("Enter the ticker symbol of the stock: ")
try:
    peg_ratio, trailing_peg_ratio, company_name = peg_ratio(ticker)
    print(f"{company_name} PEG ratio: {peg_ratio}")
    print(f"{company_name} Trailing PEG ratio: {trailing_peg_ratio}")
except KeyError:
    print("Oops! Couldn't find PEG ratio.")
