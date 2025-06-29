---
title: Donut-Plot
date: 2025-06-29
author: Your Name
cell_count: 3
score: 0
---

```python
import matplotlib.pyplot as plt
import numpy as np
```


```python
fig, ax = plt.subplots()

size = 0.3
vals = np.array([[60, 32], [37, 40]])

cmap = plt.get_cmap("tab20c")
# https://matplotlib.org/3.3.1/tutorials/colors/colormaps.html

# print(cmap)

outer_colors = cmap(np.arange(3)*4)
inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors, wedgeprops=dict(width=size, edgecolor='w'))

ax.pie(vals.flatten(), radius=1-size, colors=inner_colors, wedgeprops=dict(width=size, edgecolor='w'))

# ax.set(aspect="equal", title='Pie plot with `ax.pie`')
plt.show()

```


    
![png](/pynotes/images/Donut-Plot_1_0.png)
    



```python

```


---
**Score: 0**