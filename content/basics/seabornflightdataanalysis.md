---
title: Seabornflightdataanalysis
date: 2025-06-27
author: Your Name
cell_count: 2
score: 0
---

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
flights = sns.load_dataset("flights")
print(flights.head())

# Pivot the dataset to a heatmap format
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")
print(flights_pivot)

# Set style
sns.set_theme(style="whitegrid")

# Create the heatmap
plt.figure(figsize=(12, 6))
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Flight Passengers per Month (1949–1960)")
plt.show()

```

       year month  passengers
    0  1949   Jan         112
    1  1949   Feb         118
    2  1949   Mar         132
    3  1949   Apr         129
    4  1949   May         121
    year   1949  1950  1951  1952  1953  1954  1955  1956  1957  1958  1959  1960
    month                                                                        
    Jan     112   115   145   171   196   204   242   284   315   340   360   417
    Feb     118   126   150   180   196   188   233   277   301   318   342   391
    Mar     132   141   178   193   236   235   267   317   356   362   406   419
    Apr     129   135   163   181   235   227   269   313   348   348   396   461
    May     121   125   172   183   229   234   270   318   355   363   420   472
    Jun     135   149   178   218   243   264   315   374   422   435   472   535
    Jul     148   170   199   230   264   302   364   413   465   491   548   622
    Aug     148   170   199   242   272   293   347   405   467   505   559   606
    Sep     136   158   184   209   237   259   312   355   404   404   463   508
    Oct     119   133   162   191   211   229   274   306   347   359   407   461
    Nov     104   114   146   172   180   203   237   271   305   310   362   390
    Dec     118   140   166   194   201   229   278   306   336   337   405   432
    


    
![png](/pynotes/images/seabornflightdataanalysis_0_1.png)
    



```python

```


---
**Score: 0**