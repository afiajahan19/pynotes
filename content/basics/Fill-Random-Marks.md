---
title: Fill-Random-Marks
date: 2025-06-28
author: Your Name
cell_count: 12
score: 10
---

```python
import numpy as np
import pandas as pd
```


```python
datatype = [('Science', 'int32'), ('Maths', 'int32')]
```


```python
current_values = np.zeros(3, dtype=datatype)
```


```python
current_index = ['Row '+str(i) for i in range(1, 4)]
```


```python
df = pd.DataFrame(current_values, index=current_index)
```


```python
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
      <th>Science</th>
      <th>Maths</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Row 1</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Row 2</th>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Row 3</th>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df['Science']
```




    Row 1    0
    Row 2    0
    Row 3    0
    Name: Science, dtype: int32




```python
df['Science'][0] = 45
```

    C:\Users\Afia Jahan\AppData\Local\Temp\ipykernel_25452\2542361963.py:1: FutureWarning: Series.__setitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To set a value by position, use `ser.iloc[pos] = value`
      df['Science'][0] = 45
    


```python
df['Maths'][1] = 100
```

    C:\Users\Afia Jahan\AppData\Local\Temp\ipykernel_25452\981075704.py:1: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
    You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
    A typical example is when you are setting values in a column of a DataFrame, like:
    
    df["col"][row_indexer] = value
    
    Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
    
      df['Maths'][1] = 100
    C:\Users\Afia Jahan\AppData\Local\Temp\ipykernel_25452\981075704.py:1: FutureWarning: Series.__setitem__ treating keys as positions is deprecated. In a future version, integer keys will always be treated as labels (consistent with DataFrame behavior). To set a value by position, use `ser.iloc[pos] = value`
      df['Maths'][1] = 100
    


```python
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
      <th>Science</th>
      <th>Maths</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Row 1</th>
      <td>45</td>
      <td>0</td>
    </tr>
    <tr>
      <th>Row 2</th>
      <td>0</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Row 3</th>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (3, 2)




```python

```


---
**Score: 10**