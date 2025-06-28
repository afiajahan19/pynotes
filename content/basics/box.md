---
title: Box
date: 2025-06-28
author: Your Name
cell_count: 8
score: 5
---

```python
import pandas as pd
import numpy as np
```


```python
abc = np.array([
    [9, 13, 10],
    [7, 12, 9],
    [19, 11, 8]
])
```


```python
abc
```




    array([[ 9, 13, 10],
           [ 7, 12,  9],
           [19, 11,  8]])




```python
df2 = pd.DataFrame(abc, columns=['breakfast', 'lunch', 'dinner'])
```


```python
df2.plot.bar()
```




    <Axes: >




    
![png](/pynotes/images/box_4_1.png)
    



```python
df2.plot.barh()
```




    <Axes: >




    
![png](/pynotes/images/box_5_1.png)
    



```python
df2.plot.barh(stacked=True)
```




    <Axes: >




    
![png](/pynotes/images/box_6_1.png)
    



```python

```


---
**Score: 5**