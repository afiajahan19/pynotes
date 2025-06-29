---
title: Remove-Item-On-Loop
date: 2025-06-29
author: Your Name
cell_count: 10
score: 10
---

```python
list = [
    1, 2, 3, 4, 5, 6
]
```


```python
for i, j in enumerate(list):
    print(i, j)
```

    0 1
    1 2
    2 3
    3 4
    4 5
    5 6
    


```python
for i, j in enumerate(list):
    if(j % 2 == 0):
        del list[i]
```


```python
list
```




    [1, 3, 5]




```python
# Short form
new_list = [x for x in list if x % 2 == 1]
```


```python
new_list
```




    [1, 3, 5]




```python
list = [1, 2, 3, 4, 5, 6, 7, 8]
```


```python
from itertools import filterfalse

list[:] = filterfalse((lambda x: x%3), list)
```


```python
list
```




    [3, 6]




```python

```


---
**Score: 10**