import yfinance as yf

def get_peg_ratio(ticker):
    stock_info = yf.Ticker(ticker).info
    pe_ratio = stock_info["trailingPE"]
    eps_growth_rate = stock_info["earningsQuarterlyGrowth"]
    peg_ratio = pe_ratio / eps_growth_rate
    print(f"PE: {pe_ratio}\nEPS Growth: {eps_growth_rate}")
    return peg_ratio

ticker = input("Enter the ticker symbol of the stock: ")
peg_ratio = get_peg_ratio(ticker)
print(f"The PEG ratio of {ticker} is {peg_ratio:.2f}.")
