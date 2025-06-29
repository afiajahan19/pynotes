---
title: Bollinger-Symbol
date: 2025-06-29
author: Your Name
cell_count: 11
score: 10
---

```python
# Import necessary libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Ensure plots show in notebook
%matplotlib inline

```


```python
# Define a function to calculate Bollinger Bands
def bollinger_bands(data, window=20, num_sd=2):
    rolling_mean = data['Close'].rolling(window=window).mean()
    rolling_std = data['Close'].rolling(window=window).std()

    data['Upper Band'] = rolling_mean + (rolling_std * num_sd)
    data['Lower Band'] = rolling_mean - (rolling_std * num_sd)
    data['Moving Average'] = rolling_mean

    return data


```


```python
# Plot the Bollinger Bands
def plot_bollinger(data, symbol):
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['Upper Band'], label='Upper Band', color='red', linestyle='--')
    plt.plot(data['Lower Band'], label='Lower Band', color='green', linestyle='--')
    plt.plot(data['Moving Average'], label='Moving Average', color='orange')
    plt.fill_between(data.index, data['Lower Band'], data['Upper Band'], color='gray', alpha=0.2)
    plt.title(f'Bollinger Bands for {symbol}')
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

```


```python
# Complete function to show Bollinger Bands for a given stock symbol
def show_bollinger_bands(symbol, start="1976-01-01", end="2013-12-31", window=20, num_sd=2):
    # Download historical stock data with adjusted prices
    data = yf.download(symbol, start=start, end=end, auto_adjust=True)

    # Calculate Bollinger Bands
    data = bollinger_bands(data, window=window, num_sd=num_sd)

    # Plot the result
    plot_bollinger(data, symbol)

```


```python
# Example: Show Bollinger Bands for Autodesk (ADSK)
show_bollinger_bands("ADSK")

```

    [*********************100%***********************]  1 of 1 completed
    


    
![png](/pynotes/images/bollinger-symbol_4_1.png)
    



```python
def show_bollinger_bands(symbol):

    # Step 1: Download data
    start = "1976-01-01"
    end = "2013-12-31"

    # Download historical data
    data = yf.download(symbol, start=start, end=end)

    # Step 2: Define a function to calculate Bollinger Bands
    def bollinger_bands(price, window=20, num_sd=2):
        rolling_mean = price['Close'].rolling(window=window).mean()
        rolling_std = price['Close'].rolling(window=window).std()

        price['Upper Band'] = rolling_mean + (rolling_std * num_sd)
        price['Lower Band'] = rolling_mean - (rolling_std * num_sd)
        price['Moving Average'] = rolling_mean

        return price

    # Apply the function
    data = bollinger_bands(data)

    # Step 3: Plot the data with Bollinger Bands
    plt.figure(figsize=(12, 6))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['Upper Band'], label='Upper Band', color='red', linestyle='--')
    plt.plot(data['Lower Band'], label='Lower Band', color='green', linestyle='--')
    plt.plot(data['Moving Average'], label='Moving Average', color='orange')
    plt.fill_between(data.index, data['Lower Band'], data['Upper Band'], color='gray', alpha=0.2)
    plt.title(f'Bollinger Bands for {symbol}')
    plt.legend(loc='best')
    plt.show()
```


```python
show_bollinger_bands("ALLE")
```

    C:\Users\Afia Jahan\AppData\Local\Temp\ipykernel_68908\3736596034.py:8: FutureWarning: YF.download() has changed argument auto_adjust default to True
      data = yf.download(symbol, start=start, end=end)
    [*********************100%***********************]  1 of 1 completed
    


    
![png](/pynotes/images/bollinger-symbol_6_1.png)
    



```python
show_bollinger_bands("AIZ")
```

    C:\Users\Afia Jahan\AppData\Local\Temp\ipykernel_68908\3736596034.py:8: FutureWarning: YF.download() has changed argument auto_adjust default to True
      data = yf.download(symbol, start=start, end=end)
    [*********************100%***********************]  1 of 1 completed
    


    
![png](/pynotes/images/bollinger-symbol_7_1.png)
    



```python
show_bollinger_bands("ADSK")
```

    C:\Users\Afia Jahan\AppData\Local\Temp\ipykernel_68908\3736596034.py:8: FutureWarning: YF.download() has changed argument auto_adjust default to True
      data = yf.download(symbol, start=start, end=end)
    [*********************100%***********************]  1 of 1 completed
    


    
![png](/pynotes/images/bollinger-symbol_8_1.png)
    



```python
show_bollinger_bands("AMZN")
```

    C:\Users\Afia Jahan\AppData\Local\Temp\ipykernel_68908\3736596034.py:8: FutureWarning: YF.download() has changed argument auto_adjust default to True
      data = yf.download(symbol, start=start, end=end)
    [*********************100%***********************]  1 of 1 completed
    


    
![png](/pynotes/images/bollinger-symbol_9_1.png)
    



```python

```


---
**Score: 10**