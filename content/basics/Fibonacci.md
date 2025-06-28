---
title: Fibonacci
date: 2025-06-28
author: Your Name
cell_count: 7
score: 5
---

```python
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

```


```python
print(fib(0))  # Expected output: 0
print(fib(1))  # Expected output: 1

```

    0
    1
    


```python
print(fib(8))  # Expected output: 21

```

    21
    


```python
def fib_list(n):
    return [fib(i) for i in range(n + 1)]

print(fib_list(8))  # Expected output: [0, 1, 1, 2, 3, 5, 8, 13, 21]

```

    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    


```python
def fib_iterative(n):
    a, b = 0, 1
    seq = []
    for _ in range(n + 1):
        seq.append(a)
        a, b = b, a + b
    return seq

print(fib_iterative(8))  # [0, 1, 1, 2, 3, 5, 8, 13, 21]

```

    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    


```python
import time

n = 30

start = time.time()
print(f"Recursive fib({n}) =", fib(n))
print("Time taken (recursive):", time.time() - start)

start = time.time()
print(f"Iterative fib_list({n}) =", fib_iterative(n)[n])
print("Time taken (iterative):", time.time() - start)

```

    Recursive fib(30) = 832040
    Time taken (recursive): 0.30800914764404297
    Iterative fib_list(30) = 832040
    Time taken (iterative): 0.0
    


```python

```


---
**Score: 5**