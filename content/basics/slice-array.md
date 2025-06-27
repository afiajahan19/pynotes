---
title: Slice-Array
date: 2025-06-27
author: Your Name
cell_count: 2
score: 0
---

```python
import numpy as np

# Create a 2D array
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("Original Array:")
print(a)

# Slice a specific row
print("\nFirst row:")
print(a[0])

# Slice a specific column
print("\nSecond column:")
print(a[:, 1])

# Slice a sub-matrix
print("\nSub-matrix (first two rows and columns):")
print(a[0:2, 0:2])

# Reverse the array
print("\nReversed array (rows and columns):")
print(a[::-1, ::-1])

```

    Original Array:
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    
    First row:
    [1 2 3]
    
    Second column:
    [2 5 8]
    
    Sub-matrix (first two rows and columns):
    [[1 2]
     [4 5]]
    
    Reversed array (rows and columns):
    [[9 8 7]
     [6 5 4]
     [3 2 1]]
    


```python

```


---
**Score: 0**