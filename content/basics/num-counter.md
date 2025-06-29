---
title: Num-Counter
date: 2025-06-29
author: Your Name
cell_count: 8
score: 5
---

```python
from collections import defaultdict
```


```python
counter = defaultdict(int)
```


```python
content = "one 2 1 three 4 2 1 7 6 six 8 9 8"
```


```python
content
```




    'one 2 1 three 4 2 1 7 6 six 8 9 8'




```python
for c in content.split(' '):
    if(c.isdigit()):
        counter[c] += 1
```


```python
counter
```




    defaultdict(int, {'2': 2, '1': 2, '4': 1, '7': 1, '6': 1, '8': 2, '9': 1})




```python
for k, v in counter.items():
    print(k, "==>", v)
```

    2 ==> 2
    1 ==> 2
    4 ==> 1
    7 ==> 1
    6 ==> 1
    8 ==> 2
    9 ==> 1
    


```python

```


---
**Score: 5**