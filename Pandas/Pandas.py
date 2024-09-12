# import pandas as pd
#
# data= {
#   'Name': [ 'Shobhit', 'Rishi' ,'Harshal', 'Harshal','Shobhit'],
#   'Age': [26, 25, 23, 23, 26 ]
# }
# df = pd.DataFrame(data)
# g = df.groupby('Name').agg(
#   {
#     'Age':'max'
#   }
#
# )
# dp = df.drop_duplicates().reset_index(drop= True)
# print(dp)
# # print(g)
# # print(g.index)
# # print(df)
# filter_ = df['Age'] > 21
# # print(df[filter_])

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the stock symbol (e.g., RELIANCE.NS for Reliance Industries on NSE)
stock_symbol = 'RELIANCE.NS'

# Fetch historical stock data
data = yf.download(stock_symbol, start="2023-01-01", end="2023-12-31")

# Calculate moving averages (20-day and 50-day)
data['20_MA'] = data['Close'].rolling(window=20).mean()
data['50_MA'] = data['Close'].rolling(window=50).mean()

# Plot the stock prices and moving averages
plt.figure(figsize=(12, 6))

# Plot the closing prices
plt.plot(data['Close'], label='Closing Price', color='blue')

# Plot 20-day moving average
plt.plot(data['20_MA'], label='20-Day Moving Average', color='orange')

# Plot 50-day moving average
plt.plot(data['50_MA'], label='50-Day Moving Average', color='green')

# Add labels and title
plt.title(f'Moving Averages and Stock Prices for {stock_symbol}')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()

# Display the plot
plt.show()
