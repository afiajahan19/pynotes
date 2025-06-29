---
title: Numpy
date: 2025-06-29
author: Your Name
cell_count: 240
score: 240
---

```python
import numpy as np
a = np.array([1, 2, 3])
print(a)
```

    [1 2 3]
    


```python
b = np.array([[1, 2], [3, 4]])
print(b)
```

    [[1 2]
     [3 4]]
    


```python
c = np.zeros((2, 3))
print(c)
```

    [[0. 0. 0.]
     [0. 0. 0.]]
    


```python
d = np.ones((3, 3))
print(d)
```

    [[1. 1. 1.]
     [1. 1. 1.]
     [1. 1. 1.]]
    


```python
e = np.full((2, 2), 7)
print(e)
```

    [[7 7]
     [7 7]]
    


```python
f = np.eye(4)
print(f)
```

    [[1. 0. 0. 0.]
     [0. 1. 0. 0.]
     [0. 0. 1. 0.]
     [0. 0. 0. 1.]]
    


```python
g = np.random.rand(2, 3)
print(g)
```

    [[0.04927822 0.11759621 0.49047753]
     [0.90124012 0.36407857 0.2998955 ]]
    


```python
h = np.random.randint(0, 10, (3, 3))
print(h)
```

    [[6 4 2]
     [1 6 0]
     [2 8 6]]
    


```python
i = np.arange(0, 10, 2)
print(i)
```

    [0 2 4 6 8]
    


```python
j = np.linspace(0, 1, 5)
print(j)
```

    [0.   0.25 0.5  0.75 1.  ]
    


```python
print(a.shape)
```

    (3,)
    


```python
print(b.ndim)

```

    2
    


```python
print(c.size)

```

    6
    


```python
print(d.dtype)
```

    float64
    


```python
reshaped = np.reshape(h, (1, 9))
print(reshaped)
```

    [[6 4 2 1 6 0 2 8 6]]
    


```python
print(h.flatten())

```

    [6 4 2 1 6 0 2 8 6]
    


```python
print(h.flatten())

```

    [6 4 2 1 6 0 2 8 6]
    


```python
float_arr = a.astype(float)
print(float_arr)
```

    [1. 2. 3.]
    


```python
print(a.nbytes)

```

    24
    


```python
view = h.view()
print(view)
```

    [[6 4 2]
     [1 6 0]
     [2 8 6]]
    


```python
print(a[1])
```

    2
    


```python
print(a[1:3])

```

    [2 3]
    


```python
print(b[0:2, 1])
```

    [2 4]
    


```python
print(a[a > 1])
```

    [2 3]
    


```python
print(a[[0, 2]])

```

    [1 3]
    


```python
a[0] = 10
print(a)
```

    [10  2  3]
    


```python
a[a > 5] = 0
print(a)
```

    [0 2 3]
    


```python
print(b[1])

```

    [3 4]
    


```python
print(b[:, 0])
```

    [1 3]
    


```python
print(np.arange(10)[::2])
```

    [0 2 4 6 8]
    


```python
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y)
```

    [5 7 9]
    


```python
print(x - y)

```

    [-3 -3 -3]
    


```python
print(x * y)
```

    [ 4 10 18]
    


```python
print(y / x)
```

    [4.  2.5 2. ]
    


```python
print(x ** 2)

```

    [1 4 9]
    


```python
print(np.dot(x, y))
```

    32
    


```python
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[2, 0], [1, 2]])
print(np.matmul(mat1, mat2))
```

    [[ 4  4]
     [10  8]]
    


```python
print(np.sum(mat1))
```

    10
    


```python
print(np.mean(x))
```

    2.0
    


```python
print(np.std(x))
```

    0.816496580927726
    


```python
arr = np.array([1, 2, 3])
print(arr + 5)

```

    [6 7 8]
    


```python
print(arr * 3)


```

    [3 6 9]
    


```python
mat = np.array([[1, 2, 3], [4, 5, 6]])
print(mat + arr)
```

    [[2 4 6]
     [5 7 9]]
    


```python
print(np.sqrt(arr))
```

    [1.         1.41421356 1.73205081]
    


```python
print(np.exp(arr))
```

    [ 2.71828183  7.3890561  20.08553692]
    


```python
print(np.log(arr + 1))  
```

    [0.69314718 1.09861229 1.38629436]
    


```python
print(np.sin(arr))
```

    [0.84147098 0.90929743 0.14112001]
    


```python
print(np.cos(arr))
```

    [ 0.54030231 -0.41614684 -0.9899925 ]
    


```python
print(np.abs([-1, -2, 3]))
```

    [1 2 3]
    


```python
print(np.round([1.4, 2.6, 3.1]))
```

    [1. 3. 3.]
    


```python
print(np.min(mat))

```

    1
    


```python
print(np.max(mat))

```

    6
    


```python
print(np.argmin(mat))
```

    0
    


```python
print(np.argmax(mat))
```

    5
    


```python
print(np.sum(mat, axis=0))
```

    [5 7 9]
    


```python
print(np.sum(mat, axis=0))
```

    [5 7 9]
    


```python
print(np.mean(mat, axis=1))

```

    [2. 5.]
    


```python
print(np.cumsum(arr))
```

    [1 3 6]
    


```python
print(np.cumprod(arr))

```

    [1 2 6]
    


```python
print(np.median(mat))
```

    3.5
    


```python
square = np.array([[1, 2], [3, 4]])
print(np.linalg.det(square))
```

    -2.0000000000000004
    


```python
print(np.linalg.inv(square))
```

    [[-2.   1. ]
     [ 1.5 -0.5]]
    


```python
print(np.linalg.matrix_rank(square))
```

    2
    


```python
eig_vals, eig_vecs = np.linalg.eig(square)
print(eig_vals)

```

    [-0.37228132  5.37228132]
    


```python
print(eig_vecs)
```

    [[-0.82456484 -0.41597356]
     [ 0.56576746 -0.90937671]]
    


```python
A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])
x = np.linalg.solve(A, b)
print(x)

```

    [2. 3.]
    


```python
v = np.array([3, 4])
print(np.linalg.norm(v))
```

    5.0
    


```python
print(np.trace(square))
```

    5
    


```python
q, r = np.linalg.qr(square)
print(q)

```

    [[-0.31622777 -0.9486833 ]
     [-0.9486833   0.31622777]]
    


```python
u, s, vh = np.linalg.svd(square)
print(s)
```

    [5.4649857  0.36596619]
    


```python
print(np.any(arr > 2))
```

    True
    


```python
print(np.all(arr > 0))
```

    True
    


```python
x = np.array([True, False, True])
y = np.array([False, False, True])
print(np.logical_and(x, y))
```

    [False False  True]
    


```python
print(np.logical_or(x, y))

```

    [ True False  True]
    


```python
print(np.logical_not(x))
```

    [False  True False]
    


```python
z = np.array([1, 2, 3])
print(np.where(z > 1, 'yes', 'no'))
```

    ['no' 'yes' 'yes']
    


```python
print(np.count_nonzero([0, 1, 2, 0]))
```

    2
    


```python
a = np.array([1, 1, 2, 3, 3])
print(np.unique(a))
```

    [1 2 3]
    


```python
print(np.array_equal([1, 2], [1, 2]))

```

    True
    


```python
print(np.greater([1, 3, 5], [2, 3, 1]))
```

    [False False  True]
    


```python
a = np.array([3, 1, 2])
print(np.sort(a))

```

    [1 2 3]
    


```python
b = np.array([[3, 1], [2, 4]])
print(np.sort(b, axis=1))

```

    [[1 3]
     [2 4]]
    


```python
print(np.argsort(a))
```

    [1 2 0]
    


```python
c = np.array([1, 3, 5])
print(np.searchsorted(c, 4))
```

    2
    


```python
print(np.partition(a, 1))
```

    [1 2 3]
    


```python
print(np.argmax(b, axis=0))
```

    [0 1]
    


```python
print(np.argmin(b, axis=1))

```

    [1 0]
    


```python
arr = np.array([1, 5, 10])
print(np.clip(arr, 2, 8))
```

    [2 5 8]
    


```python
print(np.argsort([4, 1, 3]))
```

    [1 2 0]
    


```python
x = np.array([1, 2, 3, 4])
print(np.where(x > 2))
```

    (array([2, 3]),)
    


```python
np.save('array.npy', x)

```


```python
loaded = np.load('array.npy')
print(loaded)
```

    [1 2 3 4]
    


```python
np.savez('arrays.npz', a=x, b=arr)
```


```python
data = np.load('arrays.npz')
print(data['a'], data['b'])

```

    [1 2 3 4] [ 1  5 10]
    


```python
np.savetxt('array.txt', x)
```


```python
x2 = np.loadtxt('array.txt')
print(x2)
```

    [1. 2. 3. 4.]
    


```python
np.savetxt('custom.txt', x, delimiter=',')
```


```python
x3 = np.loadtxt('custom.txt', delimiter=',')
print(x3)
```

    [1. 2. 3. 4.]
    


```python
np.savetxt('ints.csv', np.array([[1,2],[3,4]]), fmt='%d', delimiter=',')

```


```python
ints = np.loadtxt('ints.csv', delimiter=',')
print(ints)
```

    [[1. 2.]
     [3. 4.]]
    


```python
arr = np.arange(6)
print(arr.reshape(2, 3))
```

    [[0 1 2]
     [3 4 5]]
    


```python
print(np.expand_dims(arr, axis=0))
```

    [[0 1 2 3 4 5]]
    


```python
a = np.array([[[1, 2, 3]]])
print(np.squeeze(a))
```

    [1 2 3]
    


```python
a = np.array([1, 2])
b = np.array([3, 4])
print(np.vstack((a, b)))

```

    [[1 2]
     [3 4]]
    


```python
print(np.hstack((a, b)))
```

    [1 2 3 4]
    


```python
print(np.dstack((a, b)))

```

    [[[1 3]
      [2 4]]]
    


```python
print(np.concatenate(([a], [b]), axis=0))
```

    [[1 2]
     [3 4]]
    


```python
c = np.array([1, 2, 3, 4])
print(np.split(c, 2))

```

    [array([1, 2]), array([3, 4])]
    


```python
d = np.array([[1, 2], [3, 4]])
print(np.vsplit(d, 2))
```

    [array([[1, 2]]), array([[3, 4]])]
    


```python
print(np.hsplit(d, 2))
```

    [array([[1],
           [3]]), array([[2],
           [4]])]
    


```python
print(np.random.randint(0, 100, 5))
```

    [70 31 73 73  5]
    


```python
print(np.random.random(5))
```

    [0.86299535 0.80227484 0.50713441 0.12514582 0.44064673]
    


```python
print(np.random.normal(0, 1, 5))

```

    [-0.1728129  -0.46241549 -2.18942983  0.69364206  1.09130089]
    


```python
print(np.random.choice([10, 20, 30]))
```

    20
    


```python
arr = np.array([1, 2, 3, 4])
np.random.shuffle(arr)
print(arr)
```

    [1 2 3 4]
    


```python
print(np.random.permutation([1, 2, 3, 4]))
```

    [4 2 1 3]
    


```python
np.random.seed(42)
print(np.random.rand())
```

    0.3745401188473625
    


```python
print(np.random.rand(2, 3))

```

    [[0.95071431 0.73199394 0.59865848]
     [0.15601864 0.15599452 0.05808361]]
    


```python
print(np.random.uniform(low=0, high=10, size=5))
```

    [8.66176146 6.01115012 7.08072578 0.20584494 9.69909852]
    


```python
print(np.random.binomial(n=10, p=0.5, size=5))
```

    [7 4 4 4 4]
    


```python
a = np.array([1.8, 2.5, 3.1])
print(np.floor(a))
```

    [1. 2. 3.]
    


```python
print(np.ceil(a))

```

    [2. 3. 4.]
    


```python
print(np.trunc(a))
```

    [1. 2. 3.]
    


```python
x = np.array([10, 20, 30])
y = np.array([3, 7, 9])
print(np.mod(x, y))
```

    [1 6 3]
    


```python
print(np.remainder(x, y))

```

    [1 6 3]
    


```python
print(np.gcd(12, 18))

```

    6
    


```python
print(np.lcm(6, 8))
```

    24
    


```python
print(np.power(2, 3))

```

    8
    


```python
print(np.sign([-10, 0, 10]))
```

    [-1  0  1]
    


```python
print(np.reciprocal([1, 2, 0.5]))
```

    [1.  0.5 2. ]
    


```python
arr = np.array([1, np.nan, 3])
print(np.isnan(arr))
```

    [False  True False]
    


```python
arr2 = np.array([1, np.inf, -np.inf])
print(np.isinf(arr2))
```

    [False  True  True]
    


```python
arr[np.isnan(arr)] = 0
print(arr)
```

    [1. 0. 3.]
    


```python
arr2[np.isinf(arr2)] = 9999
print(arr2)

```

    [1.000e+00 9.999e+03 9.999e+03]
    


```python
arr3 = np.array([1, 2, np.nan])
print(np.nansum(arr3))
```

    3.0
    


```python
print(np.nanmean(arr3))

```

    1.5
    


```python
print(np.nanmax(arr3))
```

    2.0
    


```python
print(np.nanmin(arr3))
```

    1.0
    


```python
m = np.array([[1, np.nan], [3, 4]])
col_means = np.nanmean(m, axis=0)
inds = np.where(np.isnan(m))
m[inds] = np.take(col_means, inds[1])
print(m)
```

    [[1. 4.]
     [3. 4.]]
    


```python
arr = np.array([1, np.nan, 2, np.nan])
print(np.isnan(arr).sum())
```

    2
    


```python
print(np.bitwise_and(5, 3)) 
```

    1
    


```python
print(np.bitwise_or(5, 3))
```

    7
    


```python
print(np.bitwise_xor(5, 3))
```

    6
    


```python
print(np.invert(np.array([0, 1, 2])))
```

    [-1 -2 -3]
    


```python
print(np.left_shift(1, 2))
```

    4
    


```python
print(np.right_shift(4, 1)) 
```

    2
    


```python
print(np.binary_repr(10, width=8))
```

    00001010
    


```python
x = np.array([True, False])
y = np.array([False, True])
print(np.logical_xor(x, y))
```

    [ True  True]
    


```python
bools = np.array([True, False])
print(bools.astype(int))

```

    [1 0]
    


```python
ints = np.array([0, 1, 2])
print(ints.astype(bool))
```

    [False  True  True]
    


```python
a = np.array([[1, 2], [3, 4]])
print(a.T)
```

    [[1 3]
     [2 4]]
    


```python
print(np.dot(a, a))

```

    [[ 7 10]
     [15 22]]
    


```python
print(np.linalg.matrix_power(a, 2))

```

    [[ 7 10]
     [15 22]]
    


```python
print(np.identity(3))
```

    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    


```python
print(np.diag(a))
```

    [1 4]
    


```python
d = np.array([1, 2, 3])
print(np.diag(d))
```

    [[1 0 0]
     [0 2 0]
     [0 0 3]]
    


```python
print(np.triu(a))
```

    [[1 2]
     [0 4]]
    


```python
print(np.tril(a))
```

    [[1 0]
     [3 4]]
    


```python
b = np.zeros((3, 3))
np.fill_diagonal(b, 1)
print(b)
```

    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    


```python
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.diag(c, k=1))
```

    [2 6]
    


```python
a = np.array([1, 2, 3, 4])
print(np.fft.fft(a))

```

    [10.+0.j -2.+2.j -2.+0.j -2.-2.j]
    


```python
f = np.fft.fft(a)
print(np.fft.ifft(f))

```

    [1.+0.j 2.+0.j 3.+0.j 4.+0.j]
    


```python
print(np.fft.fftfreq(4))

```

    [ 0.    0.25 -0.5  -0.25]
    


```python
img = np.array([[1, 2], [3, 4]])
print(np.fft.fft2(img))

```

    [[10.+0.j -2.+0.j]
     [-4.+0.j  0.+0.j]]
    


```python
f2 = np.fft.fft2(img)
print(np.fft.ifft2(f2))

```

    [[1.+0.j 2.+0.j]
     [3.+0.j 4.+0.j]]
    


```python
print(np.fft.fftshift(f2))
```

    [[ 0.+0.j -4.+0.j]
     [-2.+0.j 10.+0.j]]
    


```python
print(np.fft.ifftshift(f2))
```

    [[ 0.+0.j -4.+0.j]
     [-2.+0.j 10.+0.j]]
    


```python
f = np.fft.fft(a)
power = np.abs(f)**2
print(power)
```

    [100.   8.   4.   8.]
    


```python
phase = np.angle(f)
print(phase)
```

    [ 0.          2.35619449  3.14159265 -2.35619449]
    


```python
print(np.fft.rfft(a))
```

    [10.+0.j -2.+2.j -2.+0.j]
    


```python
a = np.array([1, 2, 2, 3])
print(np.unique(a))

```

    [1 2 3]
    


```python
b = np.array([2, 3, 4])
print(np.intersect1d(a, b))
```

    [2 3]
    


```python
print(np.union1d(a, b))
```

    [1 2 3 4]
    


```python
print(np.setdiff1d(a, b))

```

    [1]
    


```python
print(np.setxor1d(a, b))
```

    [1 4]
    


```python
unique, counts = np.unique(a, return_counts=True)
print(dict(zip(unique, counts)))
```

    {np.int64(1): np.int64(1), np.int64(2): np.int64(2), np.int64(3): np.int64(1)}
    


```python
print(set(a) == set(b))
```

    False
    


```python
print(np.asarray(list(set(a))))
```

    [1 2 3]
    


```python
arr2d = np.array([[1, 2], [1, 2], [3, 4]])
print(np.unique(arr2d, axis=0))
```

    [[1 2]
     [3 4]]
    


```python
data = np.random.randint(0, 10, 100)
hist, bins = np.histogram(data, bins=5)
print(hist)
print(bins)

```

    [18 19 14 24 25]
    [0.  1.8 3.6 5.4 7.2 9. ]
    


```python
print(np.digitize([1, 2, 6], bins=[0, 3, 6]))

```

    [1 1 3]
    


```python
print(np.histogram(data, bins=[0, 3, 6, 10]))

```

    (array([30, 21, 49]), array([ 0,  3,  6, 10]))
    


```python
hist, bins = np.histogram(data, bins=5, density=True)
print(hist)
```

    [0.1        0.10555556 0.07777778 0.13333333 0.13888889]
    


```python
hist, bins = np.histogram(data, bins=5)
cumsum = np.cumsum(hist)
print(cumsum)

```

    [ 18  37  51  75 100]
    


```python
x = np.random.rand(100)
y = np.random.rand(100)
H, xedges, yedges = np.histogram2d(x, y, bins=5)
print(H)
```

    [[2. 3. 2. 4. 7.]
     [6. 3. 8. 5. 4.]
     [1. 5. 2. 1. 6.]
     [6. 1. 2. 4. 4.]
     [5. 7. 2. 7. 3.]]
    


```python
print(hist.flatten())
```

    [18 19 14 24 25]
    


```python
values = np.array([0, 1, 1, 3, 4, 4, 4])
print(np.bincount(values))
```

    [1 2 0 1 3]
    


```python
weights = np.ones_like(values)
print(np.bincount(values, weights=weights))

```

    [1. 2. 0. 1. 3.]
    


```python
bins = [0, 1, 2, 3, 4, 5]
print(np.digitize([0.5, 2.2, 3.9], bins))
```

    [1 3 4]
    


```python
x = np.array([1, 2, 3])
y = np.array([4, 5])
X, Y = np.meshgrid(x, y)
print(X)
print(Y)
```

    [[1 2 3]
     [1 2 3]]
    [[4 4 4]
     [5 5 5]]
    


```python
i, j = np.indices((2, 3))
print(i)
print(j)

```

    [[0 0 0]
     [1 1 1]]
    [[0 1 2]
     [0 1 2]]
    


```python
og = np.ogrid[0:3, 0:2]
print(og[0])
print(og[1])
```

    [[0]
     [1]
     [2]]
    [[0 1]]
    


```python
mg = np.mgrid[0:3, 0:2]
print(mg)
```

    [[[0 0]
      [1 1]
      [2 2]]
    
     [[0 1]
      [0 1]
      [0 1]]]
    


```python
X, Y = np.meshgrid(np.linspace(-1, 1, 5), np.linspace(-1, 1, 5))
Z = X**2 + Y**2
print(Z)
```

    [[2.   1.25 1.   1.25 2.  ]
     [1.25 0.5  0.25 0.5  1.25]
     [1.   0.25 0.   0.25 1.  ]
     [1.25 0.5  0.25 0.5  1.25]
     [2.   1.25 1.   1.25 2.  ]]
    


```python
x = np.linspace(0, 1, 3)
y = np.linspace(0, 1, 3)
z = np.linspace(0, 1, 3)
X, Y, Z = np.meshgrid(x, y, z)
print(X.shape)

```

    (3, 3, 3)
    


```python
xi, yi = np.meshgrid([1, 2], [3, 4], indexing='ij')
print(xi)
print(yi)
```

    [[1 1]
     [2 2]]
    [[3 4]
     [3 4]]
    


```python
x = [1, 2]
y = [3, 4]
X, Y = np.meshgrid(x, y)
print(np.array([X.ravel(), Y.ravel()]).T)
```

    [[1 3]
     [2 3]
     [1 4]
     [2 4]]
    


```python
r = np.linspace(0, 1, 5)
theta = np.linspace(0, 2 * np.pi, 5)
R, T = np.meshgrid(r, theta)
print(R)
print(T)
```

    [[0.   0.25 0.5  0.75 1.  ]
     [0.   0.25 0.5  0.75 1.  ]
     [0.   0.25 0.5  0.75 1.  ]
     [0.   0.25 0.5  0.75 1.  ]
     [0.   0.25 0.5  0.75 1.  ]]
    [[0.         0.         0.         0.         0.        ]
     [1.57079633 1.57079633 1.57079633 1.57079633 1.57079633]
     [3.14159265 3.14159265 3.14159265 3.14159265 3.14159265]
     [4.71238898 4.71238898 4.71238898 4.71238898 4.71238898]
     [6.28318531 6.28318531 6.28318531 6.28318531 6.28318531]]
    


```python
phi = np.linspace(0, np.pi, 3)
theta = np.linspace(0, 2 * np.pi, 4)
PHI, THETA = np.meshgrid(phi, theta)
print(PHI)
print(THETA)
```

    [[0.         1.57079633 3.14159265]
     [0.         1.57079633 3.14159265]
     [0.         1.57079633 3.14159265]
     [0.         1.57079633 3.14159265]]
    [[0.         0.         0.        ]
     [2.0943951  2.0943951  2.0943951 ]
     [4.1887902  4.1887902  4.1887902 ]
     [6.28318531 6.28318531 6.28318531]]
    


```python
dt = np.dtype([('name', 'U10'), ('age', 'i4')])
people = np.array([('Alice', 25), ('Bob', 30)], dtype=dt)
print(people)
```

    [('Alice', 25) ('Bob', 30)]
    


```python
print(people['name'])
```

    ['Alice' 'Bob']
    


```python
sorted_people = np.sort(people, order='age')
print(sorted_people)
```

    [('Alice', 25) ('Bob', 30)]
    


```python
print(people[people['age'] > 25])

```

    [('Bob', 30)]
    


```python
print(people[people['age'] > 25])

```

    [('Bob', 30)]
    


```python
new = np.array([('Charlie', 22)], dtype=dt)
people = np.concatenate((people, new))
print(people)
```

    [('Alice', 25) ('Bob', 30) ('Charlie', 22)]
    


```python
dt_nested = np.dtype([('coords', [('x', 'f4'), ('y', 'f4')]), ('value', 'i4')])
data = np.array([((1.0, 2.0), 10)], dtype=dt_nested)
print(data)

```

    [((1., 2.), 10)]
    


```python
print(people[['name', 'age']])
```

    [('Alice', 25) ('Bob', 30) ('Charlie', 22)]
    


```python
import numpy.ma as ma
data = ma.array([1, 2, 3], mask=[0, 1, 0])
print(data)

```

    [1 -- 3]
    


```python
print(data.mask)
```

    [False  True False]
    


```python
print(data.mean())
```

    2.0
    


```python
print(data.filled(-1))
```

    [ 1 -1  3]
    


```python
masked = ma.masked_equal([1, -99, 3], -99)
print(masked)
```

    [1 -- 3]
    


```python
x = np.array([1, 2, 3, 4])
masked = ma.masked_where(x > 2, x)
print(masked)
```

    [1 2 -- --]
    


```python
a = ma.masked_less([1, 2, 3], 2)
b = ma.masked_greater([1, 2, 3], 2)
combined = ma.mask_or(a.mask, b.mask)
print(combined)
```

    [ True False  True]
    


```python
print(data.compressed())

```

    [1 3]
    


```python
print(ma.std(masked))
```

    0.5
    


```python
matrix = np.array([[1, 2], [3, 4]])
row = np.array([10, 20])
print(matrix + row)

```

    [[11 22]
     [13 24]]
    


```python
col = np.array([[1], [2]])
print(matrix - col)
```

    [[0 1]
     [1 2]]
    


```python
a = np.array([1, 2])
b = np.array([3, 4])
print(np.outer(a, b))

```

    [[3 4]
     [6 8]]
    


```python
arr = np.array([1, 2, 3])
print(arr[:, None] + arr)
```

    [[2 3 4]
     [3 4 5]
     [4 5 6]]
    


```python
m = np.array([[1, 2], [3, 4]])
norms = np.linalg.norm(m, axis=1, keepdims=True)
print(m / norms)
```

    [[0.4472136  0.89442719]
     [0.6        0.8       ]]
    


```python
x = np.array([1, 2, 3])
y = 2
print(x == y)

```

    [False  True False]
    


```python
a = np.ones((3, 3))
b = np.array([1, 2, 3])
print(a * b[:, np.newaxis])
```

    [[1. 1. 1.]
     [2. 2. 2.]
     [3. 3. 3.]]
    


```python
dates = np.array(['2025-06-01', '2025-06-10'], dtype='datetime64[D]')
print(dates)
```

    ['2025-06-01' '2025-06-10']
    


```python
print(np.arange('2025-01', '2025-04', dtype='datetime64[M]'))
```

    ['2025-01' '2025-02' '2025-03']
    


```python
print(dates + np.timedelta64(5, 'D'))
```

    ['2025-06-06' '2025-06-15']
    


```python
print(dates[1] - dates[0])

```

    9 days
    


```python
delta = np.array(['2025-06-10'], dtype='datetime64[D]') - np.array(['2025-06-01'], dtype='datetime64[D]')
print(delta.astype(int))
```

    [9]
    


```python
print(np.datetime64('today', 'D'))
```

    2025-06-29
    


```python
print(np.arange('2025-01', '2026-01', dtype='datetime64[M]'))

```

    ['2025-01' '2025-02' '2025-03' '2025-04' '2025-05' '2025-06' '2025-07'
     '2025-08' '2025-09' '2025-10' '2025-11' '2025-12']
    


```python
months = np.arange('2025-01', '2025-04', dtype='datetime64[M]')
print(np.diff(months))
```

    [1 1]
    


```python
x = np.arange(1000000)
print(x * 2)
```

    [      0       2       4 ... 1999994 1999996 1999998]
    


```python
arr = np.array([1, 2, 3])
print(np.where(arr > 2, 100, 0))
```

    [  0   0 100]
    


```python
arr = np.arange(10)
view = arr.view()
print(view.base is arr) 
```

    True
    


```python
a = np.array([1, 2, 3])
b = a.view()
b[0] = 100
print(a)
```

    [100   2   3]
    


```python
x = np.arange(1000000)
print(x[::100])
```

    [     0    100    200 ... 999700 999800 999900]
    


```python
x = np.array([1, 2, 3])
x *= 2
print(x)
```

    [2 4 6]
    


```python
x = np.array([1.0, 2.0, 3.0])
y = np.empty_like(x)
np.add(x, x, out=y)
print(y)
```

    [2. 4. 6.]
    


```python
a = np.array([1.00001, 1.00002])
b = np.array([1.00002, 1.00001])
print(np.allclose(a, b, atol=1e-4))
```

    True
    


```python

```


---
**Score: 240**