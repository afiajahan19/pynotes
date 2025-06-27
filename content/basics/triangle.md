---
title: Triangle
date: 2025-06-27
author: Your Name
cell_count: 3
score: 0
---

```python
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in reversed(range(len(triangle) - 1)):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j],
                                      triangle[i + 1][j + 1])
        return triangle[0][0]

# Example triangle input
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

# Create an instance of Solution and call the method
sol = Solution()
result = sol.minimumTotal(triangle)
print("Minimum path sum:", result)


```

    Minimum path sum: 11
    


```python

```


```python

```


---
**Score: 0**