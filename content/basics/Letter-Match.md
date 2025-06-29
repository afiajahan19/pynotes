---
title: Letter-Match
date: 2025-06-29
author: Your Name
cell_count: 4
score: 0
---

```python
import re
```


```python
contents = [
    "AB23",
    "A2B3", 
    "DE09",
    "MN90",
    "XYi9",
    "XY90"
]
```


```python
for content in contents:
    regex_pattern = "(?:AB|DE|XY)\d+" 
    # starts with AB or DE; should contain one or more number

    m = re.match(regex_pattern, content)

    if(m):
        print('matched : '+content)
```

    matched : AB23
    matched : DE09
    matched : XY90
    

    <>:2: SyntaxWarning: invalid escape sequence '\d'
    <>:2: SyntaxWarning: invalid escape sequence '\d'
    C:\Users\Afia Jahan\AppData\Local\Temp\ipykernel_75024\3010093568.py:2: SyntaxWarning: invalid escape sequence '\d'
      regex_pattern = "(?:AB|DE|XY)\d+"
    


```python

```


---
**Score: 0**