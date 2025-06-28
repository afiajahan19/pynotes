---
title: Seaborn-Pynotes-Growth
date: 2025-06-28
author: Your Name
cell_count: 7
score: 5
---

```python
!pip install seaborn

```

    Requirement already satisfied: seaborn in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (0.13.2)
    Requirement already satisfied: numpy!=1.24.0,>=1.20 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from seaborn) (1.26.4)
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
    


```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

```


```python
days_list = [
    1, 1, 1, 
    2, 2, 2,
    3, 3, 3
]
learners_list = [
    'raja', 'hari', 'steve', 
    'raja', 'hari', 'steve',
    'raja', 'hari', 'steve'
]
score_list = [
    0, 0, 0, 
    50, 40, 60,
    60, 45, 60
]

data = {
    'days' : days_list,
    'learners' : learners_list,
    'score' : score_list
}

df = pd.DataFrame(data)
df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>days</th>
      <th>learners</th>
      <th>score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>raja</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>hari</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>steve</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>raja</td>
      <td>50</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>hari</td>
      <td>40</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2</td>
      <td>steve</td>
      <td>60</td>
    </tr>
    <tr>
      <th>6</th>
      <td>3</td>
      <td>raja</td>
      <td>60</td>
    </tr>
    <tr>
      <th>7</th>
      <td>3</td>
      <td>hari</td>
      <td>45</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3</td>
      <td>steve</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
df_wide = df.pivot(index="days", columns="learners", values="score")
df_wide

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>learners</th>
      <th>hari</th>
      <th>raja</th>
      <th>steve</th>
    </tr>
    <tr>
      <th>days</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40</td>
      <td>50</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>45</td>
      <td>60</td>
      <td>60</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.set_theme(style="darkgrid")  # other options: "whitegrid", "dark", etc.

```


```python
sns.lineplot(data=df_wide)
plt.title("Learners' Score over Days (Wide Format)")
plt.ylabel("Score")
plt.xlabel("Days")
plt.show()

```


    
![png](/pynotes/images/seaborn-pynotes-growth_5_0.png)
    



```python

```


---
**Score: 5**