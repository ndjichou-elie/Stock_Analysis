import yfinance as yf
import pandas as pd

# Fetch Tesla stock data
tesla_data = yf.Ticker("TSLA")

# Get historical stock data
tesla_df = tesla_data.history(period="max")

# Reset index
tesla_df.reset_index(inplace=True)

# Save the data
tesla_df.to_csv("Tesla_Stock_Data.csv", index=False)

# Display first 5 rows
print(tesla_df.head())
