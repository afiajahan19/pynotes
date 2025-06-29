---
title: Match-All-String
date: 2025-06-29
author: Your Name
cell_count: 8
score: 5
---

```python
one = "Toronto is nice"
```


```python
one
```




    'Toronto is nice'




```python
one_array = one.split(" ")
```


```python
two = "It is nice to be in Toronto"
```


```python
two_array = two.split(" ")
```


```python
two_array

```




    ['It', 'is', 'nice', 'to', 'be', 'in', 'Toronto']




```python
all(x in two for x in one_array)
```




    True




```python

```


---
**Score: 5**