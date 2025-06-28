---
title: Slice-Array
date: 2025-06-28
author: Your Name
cell_count: 17
score: 15
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
# Create a list of numbers
a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a
```




    [10, 20, 30, 40, 50, 60, 70, 80, 90]




```python
# Check the type of 'a'
type(a)

```




    list




```python
# Get elements from index 4 to 7 (not including 8)
a[4:8]
# Output: [50, 60, 70, 80]

```




    [50, 60, 70, 80]




```python
# Get first 4 items
a[:4]
# Output: [10, 20, 30, 40]

```




    [10, 20, 30, 40]




```python
# Get all elements from index 4 to the end
a[4:]
# Output: [50, 60, 70, 80, 90]

```




    [50, 60, 70, 80, 90]




```python
# Get a full copy of the list
a[:]
# Output: [10, 20, 30, 40, 50, 60, 70, 80, 90]

```




    [10, 20, 30, 40, 50, 60, 70, 80, 90]




```python
# Last item
a[-1]
# Output: 90

# Second last item
a[-2]
# Output: 80

```




    80




```python
# Last 2 items
a[-2:]
# Output: [80, 90]

# Everything except last 2 items
a[:-2]
# Output: [10, 20, 30, 40, 50, 60, 70]

```




    [10, 20, 30, 40, 50, 60, 70]




```python
# All items reversed
a[::-1]
# Output: [90, 80, 70, 60, 50, 40, 30, 20, 10]

```




    [90, 80, 70, 60, 50, 40, 30, 20, 10]




```python
# First two items in reverse
a[1::-1]
# Output: [20, 10]

# First two items reversed with step -2
a[1::-2]
# Output: [20]

```




    [20]




```python
# Get the first three items reversed
a[2::-1]
# Output: [30, 20, 10]

```




    [30, 20, 10]




```python
# All items reversed except last one
a[-2::-1]
# Output: [80, 70, 60, 50, 40, 30, 20, 10]

```




    [80, 70, 60, 50, 40, 30, 20, 10]




```python
# Remove last 2 items and reverse the rest
a[-3::-1]
# Output: [70, 60, 50, 40, 30, 20, 10]

```




    [70, 60, 50, 40, 30, 20, 10]




```python
# Last two items reversed
a[:-3:-1]
# Output: [90, 80]

# Last three items reversed
a[:-4:-1]
# Output: [90, 80, 70]

```




    [90, 80, 70]




```python
# Everything except the last 3 items, reversed
a[-4::-1]
# Output: [60, 50, 40, 30, 20, 10]

```




    [60, 50, 40, 30, 20, 10]




```python

```


---
**Score: 15**