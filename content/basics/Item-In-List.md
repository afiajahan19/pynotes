---
title: Item-In-List
date: 2025-06-28
author: Your Name
cell_count: 9
score: 5
---

```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: C:\\Users\\Afia Jahan\\anaconda3\\envs\\py312; pyv: 3.12.11 | packaged by Anaconda, Inc. | (main, Jun  5 2025, 12:58:53) [MSC v.1929 64 bit (AMD64)]'




```python
print(pyu.ps2("haystack-ai ollama-haystack python-dotenv"))
```

    
    


```python
model_cache = {
    "test1.joblib" : {"one" : "two"}
}
```


```python
cache_keys = list(model_cache.keys())
```


```python
cache_keys
```




    ['test1.joblib']




```python
joblib_path = 'test1.joblib'
```


```python
joblib_path not in cache_keys
```




    False




```python
joblib_path in cache_keys
```




    True




```python

```


---
**Score: 5**