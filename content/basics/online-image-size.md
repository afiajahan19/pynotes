---
title: Online-Image-Size
date: 2025-06-29
author: Your Name
cell_count: 8
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




    
![png](/pynotes/images/online-image-size_3_0.png)
    




```python
print(img)
```

    <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=500x500 at 0x1315A029850>
    


```python
image_array = np.asarray(Image.open('temp.jpg'))
```


```python
image_array.shape
```




    (500, 500, 3)




```python

```


---
**Score: 5**