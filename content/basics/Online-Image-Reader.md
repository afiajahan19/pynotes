---
title: Online-Image-Reader
date: 2025-06-29
author: Your Name
cell_count: 5
score: 5
---

```python
from PIL import Image
import numpy as np
import urllib.request
```


```python

image_path = 'https://multimedia.bbycastatic.ca/multimedia/products/500x500/107/10736/10736343.jpg'
```


```python
with urllib.request.urlopen(image_path) as url:
    with open('temp.jpg', 'wb') as f:
        f.write(url.read())

img = Image.open('temp.jpg')
```


```python
img
```




    
![png](/pynotes/images/Online-Image-Reader_3_0.png)
    




```python

```


---
**Score: 5**