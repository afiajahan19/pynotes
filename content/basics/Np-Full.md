---
title: Np-Full
date: 2025-06-29
author: Your Name
cell_count: 7
score: 5
---

```python
import pyutil as pyu
pyu.get_local_pyinfo()
```




    'conda env: C:\\Users\\Afia Jahan\\anaconda3\\envs\\py312; pyv: 3.12.11 | packaged by Anaconda, Inc. | (main, Jun  5 2025, 12:58:53) [MSC v.1929 64 bit (AMD64)]'




```python
print(pyu.ps2("pandas"))
```

    Name: pandas
    Version: 2.3.0
    Summary: Powerful data structures for data analysis, time series, and statistics
    Home-page: https://pandas.pydata.org
    Author: 
    Author-email: The Pandas Development Team <pandas-dev@python.org>
    License: BSD 3-Clause License
    
     Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
     All rights reserved.
    
     Copyright (c) 2011-2023, Open source contributors.
    
     Redistribution and use in source and binary forms, with or without
     modification, are permitted provided that the following conditions are met:
    
     * Redistributions of source code must retain the above copyright notice, this
       list of conditions and the following disclaimer.
    
     * Redistributions in binary form must reproduce the above copyright notice,
       this list of conditions and the following disclaimer in the documentation
       and/or other materials provided with the distribution.
    
     * Neither the name of the copyright holder nor the names of its
       contributors may be used to endorse or promote products derived from
       this software without specific prior written permission.
    
     THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
     AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
     IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
     DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
     FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
     DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
     SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
     CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
     OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
     OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
    
    Location: C:\Users\Afia Jahan\anaconda3\envs\py312\Lib\site-packages
    Requires: numpy, python-dateutil, pytz, tzdata
    Required-by: farm-haystack, seaborn, yfinance
    
    


```python
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
```


```python
product
```




    24




```python
import numpy as np
```


```python
sizes = np.full((10), 7, dtype=int)
sizes
```




    array([7, 7, 7, 7, 7, 7, 7, 7, 7, 7])




```python

```


---
**Score: 5**