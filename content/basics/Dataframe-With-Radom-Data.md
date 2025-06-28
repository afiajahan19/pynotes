---
title: Dataframe-With-Radom-Data
date: 2025-06-28
author: Your Name
cell_count: 10
score: 10
---

```python
import numpy as np
import pandas as pd
import random
```


```python
def xrange(x):
    return iter(range(x))
```


```python
rnd_1 = [random.randrange(1, 20) for x in xrange(10)]
```


```python
rnd_1
```




    [5, 3, 10, 18, 10, 18, 19, 13, 1, 5]




```python
rnd_2 = [random.randrange(1, 20) for x in xrange(10)]
```


```python
rnd_2
```




    [4, 1, 3, 2, 17, 13, 7, 1, 11, 1]




```python
date = pd.date_range('2018-01-01', '2018-01-10')
```


```python
data = pd.DataFrame({
    'date' : date,
    'rnd_1' : rnd_1,
    'rnd_2' : rnd_2
})
```


```python
data
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
      <th>date</th>
      <th>rnd_1</th>
      <th>rnd_2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018-01-01</td>
      <td>5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2018-01-02</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018-01-03</td>
      <td>10</td>
      <td>3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2018-01-04</td>
      <td>18</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2018-01-05</td>
      <td>10</td>
      <td>17</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2018-01-06</td>
      <td>18</td>
      <td>13</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2018-01-07</td>
      <td>19</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2018-01-08</td>
      <td>13</td>
      <td>1</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2018-01-09</td>
      <td>1</td>
      <td>11</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2018-01-10</td>
      <td>5</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


---
**Score: 10**