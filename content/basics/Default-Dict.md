---
title: Default-Dict
date: 2025-06-29
author: Your Name
cell_count: 13
score: 10
---

```python
from collections import defaultdict
```


```python
user = defaultdict(lambda: 'Kevin')
```


```python
user
```




    defaultdict(<function __main__.<lambda>()>, {})




```python
type(user)
```




    collections.defaultdict




```python
user['abc']
```




    'Kevin'




```python
user['name'] = 'Peter'
user['age'] = 21
user['city'] = 'Toronto'
```


```python
user
```




    defaultdict(<function __main__.<lambda>()>,
                {'abc': 'Kevin', 'name': 'Peter', 'age': 21, 'city': 'Toronto'})




```python
defaultdict(<function __main__.<lambda>>,
            {'abc': 'Kevin',
             'age': 21,
             'city': 'Toronto',
             'country': 'Kevin',
             'name': 'Peter'})
```


      Cell In[8], line 1
        defaultdict(<function __main__.<lambda>>,
                    ^
    SyntaxError: invalid syntax
    



```python
from collections import defaultdict

```


```python
d = defaultdict(lambda: 'default value', {
    'abc': 'Kevin',
    'age': 21,
    'city': 'Toronto',
    'country': 'Kevin',
    'name': 'Peter'
})
```


```python
for k, v in user.items():
    print(k, "==>", v)
```

    abc ==> Kevin
    name ==> Peter
    age ==> 21
    city ==> Toronto
    


```python

```


```python

```


---
**Score: 10**