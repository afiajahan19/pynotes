---
title: Remove-Num
date: 2025-06-29
author: Your Name
cell_count: 11
score: 10
---

```python
content = '15. TFRecord in Tensorflow'
```


```python
content

```




    '15. TFRecord in Tensorflow'




```python
import re
```


```python
result = re.sub(r'\d+\.', '', content)
```


```python
result.strip()
```




    'TFRecord in Tensorflow'




```python
content2 = """1. Cross Entropy Loss Derivation

2. How to split a tensorflow model into two parts?

3. RNN Text Generation with Eager Execution

4. Softmax activation in Tensor"""
```


```python
content2
```




    '1. Cross Entropy Loss Derivation\n\n2. How to split a tensorflow model into two parts?\n\n3. RNN Text Generation with Eager Execution\n\n4. Softmax activation in Tensor'




```python
result2 = re.sub(r'\d+\.', '', content2)
```


```python
result2.strip()
```




    'Cross Entropy Loss Derivation\n\n How to split a tensorflow model into two parts?\n\n RNN Text Generation with Eager Execution\n\n Softmax activation in Tensor'




```python
for c in result2.strip().split('\n'):
    print(c.strip())
```

    Cross Entropy Loss Derivation
    
    How to split a tensorflow model into two parts?
    
    RNN Text Generation with Eager Execution
    
    Softmax activation in Tensor
    


```python

```


---
**Score: 10**