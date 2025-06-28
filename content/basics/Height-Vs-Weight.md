---
title: Height-Vs-Weight
date: 2025-06-28
author: Your Name
cell_count: 7
score: 5
---

```python
!python --version
```

    Python 3.12.11
    


```python
!pip install seaborn
```

    Requirement already satisfied: seaborn in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (0.13.2)
    Requirement already satisfied: numpy!=1.24.0,>=1.20 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from seaborn) (2.1.3)
    Requirement already satisfied: pandas>=1.2 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from seaborn) (2.3.0)
    Requirement already satisfied: matplotlib!=3.6.1,>=3.4 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from seaborn) (3.10.3)
    Requirement already satisfied: contourpy>=1.0.1 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (1.3.2)
    Requirement already satisfied: cycler>=0.10 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (0.12.1)
    Requirement already satisfied: fonttools>=4.22.0 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (4.58.4)
    Requirement already satisfied: kiwisolver>=1.3.1 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (1.4.8)
    Requirement already satisfied: packaging>=20.0 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (24.2)
    Requirement already satisfied: pillow>=8 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (11.2.1)
    Requirement already satisfied: pyparsing>=2.3.1 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (3.2.3)
    Requirement already satisfied: python-dateutil>=2.7 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib!=3.6.1,>=3.4->seaborn) (2.9.0.post0)
    Requirement already satisfied: pytz>=2020.1 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from pandas>=1.2->seaborn) (2025.2)
    Requirement already satisfied: tzdata>=2022.7 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from pandas>=1.2->seaborn) (2025.2)
    Requirement already satisfied: six>=1.5 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from python-dateutil>=2.7->matplotlib!=3.6.1,>=3.4->seaborn) (1.17.0)
    

    WARNING: Ignoring invalid distribution ~umpy (C:\Users\Afia Jahan\anaconda3\envs\py312\Lib\site-packages)
    WARNING: Ignoring invalid distribution ~umpy (C:\Users\Afia Jahan\anaconda3\envs\py312\Lib\site-packages)
    WARNING: Ignoring invalid distribution ~umpy (C:\Users\Afia Jahan\anaconda3\envs\py312\Lib\site-packages)
    


```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
```


```python
data = {
    "Height": [150, 160, 165, 170, 175, 180, 185],
    "Weight": [50, 60, 65, 70, 75, 80, 85],
    "Gender": ["Female", "Male", "Female", "Male", "Female", "Male", "Female"]
}

```


```python
df = pd.DataFrame(data)
```


```python
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
scatter_plot = sns.scatterplot(data=df, x="Height", y="Weight", hue="Gender", style="Gender", s=100)

plt.title("Height vs. Weight by Gender", fontsize=16)
plt.xlabel("Height (cm)", fontsize=12)
plt.ylabel("Weight (kg)", fontsize=12)
plt.legend(title="Gender")
plt.show(
)
```


    
![png](/pynotes/images/Height-Vs-Weight_5_0.png)
    



```python

```


---
**Score: 5**