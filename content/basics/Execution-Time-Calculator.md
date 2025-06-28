---
title: Execution-Time-Calculator
date: 2025-06-28
author: Your Name
cell_count: 5
score: 5
---

```python
import random
import time
```


```python
# PythonDecorators/entry_exit_class.py
class execution_time_calculator(object):

    def __init__(self, f):
        self.f = f

    def __call__(self):
        start = int(round(time.time() * 1000))
        print("Entering", self.f.__name__)
        self.f()
        end = int(round(time.time() * 1000))
        #print("Exited", self.f.__name__)
        print("Time taken : "+str((end-start)) + ' milli seconds')
```


```python
@execution_time_calculator
def func1():
    seconds = random.randint(5, 15)    
    print("inside func2() sleeping for "+str(seconds) + " seconds")
    time.sleep(seconds)
```


```python
func1()
```

    Entering func1
    inside func2() sleeping for 15 seconds
    Time taken : 15004 milli seconds
    


```python

```


---
**Score: 5**