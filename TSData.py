
from alpha_vantage.timeseries import TimeSeries

# Replace YOUR_API_KEY with your actual Alpha Vantage API key
ts = TimeSeries(key='YOUR_API_KEY', output_format='pandas')

# Replace SYMBOL with the ticker symbol you're interested in
data, meta_data = ts.get_daily(symbol='SYMBOL', outputsize='full')

# The data variable will contain a pandas DataFrame with the historical stock prices
print(data.head())