---
title: Untitled
date: 2025-06-27
author: Your Name
cell_count: 2
score: 0
---

```python
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Download stock data (e.g., TCS.NS)
symbol = "TCS.NS"
start_date = "2020-01-01"
end_date = "2023-01-01"

data = yf.download(symbol, start=start_date, end=end_date)

# Step 2: Calculate Bollinger Bands
window = 20  # 20-day moving average
data['SMA'] = data['Close'].rolling(window=window).mean()
data['STD'] = data['Close'].rolling(window=window).std()

data['Upper Band'] = data['SMA'] + (2 * data['STD'])
data['Lower Band'] = data['SMA'] - (2 * data['STD'])

# Step 3: Plotting
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Closing Price', color='blue')
plt.plot(data['SMA'], label='20-Day SMA', color='orange')
plt.plot(data['Upper Band'], label='Upper Bollinger Band', color='green')
plt.plot(data['Lower Band'], label='Lower Bollinger Band', color='red')

plt.fill_between(data.index, data['Upper Band'], data['Lower Band'], color='gray', alpha=0.2)

plt.title(f'Bollinger Bands for {symbol}')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend(loc='upper left')
plt.grid()
plt.tight_layout()
plt.show()

```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    Cell In[2], line 1
    ----> 1 import yfinance as yf
          2 import pandas as pd
          3 import matplotlib.pyplot as plt
    

    ModuleNotFoundError: No module named 'yfinance'



```python

```


---
**Score: 0**