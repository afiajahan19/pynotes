---
title: 5-Tuple
date: 2025-06-29
author: Your Name
cell_count: 127
score: 125
---

```python
#Tuple Basics
```


```python
t = (1, 2, 3)
print(t)
```

    (1, 2, 3)
    


```python
print(type(t))
```

    <class 'tuple'>
    


```python
t2 = tuple([4, 5, 6])
print(t2)
```

    (4, 5, 6)
    


```python
t3 = 1, 2, 3
print(t3)

```

    (1, 2, 3)
    


```python
t4 = (1,)  # single element
print(t4)
```

    (1,)
    


```python
print(len(t))
```

    3
    


```python
print(t[0])
```

    1
    


```python
print(t[-1])
```

    3
    


```python
print(t[1:3])

```

    (2, 3)
    


```python
print(t[:2])
```

    (1, 2)
    


```python
print(t[::2])
```

    (1, 3)
    


```python
print(2 in t)
```

    True
    


```python
print(5 not in t)

```

    True
    


```python
print(t + (4, 5))
```

    (1, 2, 3, 4, 5)
    


```python
print(t * 2)
```

    (1, 2, 3, 1, 2, 3)
    


```python
t_nested = (1, (2, 3))
print(t_nested[1][0])

```

    2
    


```python
print(type(()))
```

    <class 'tuple'>
    


```python
print(tuple("abc"))
```

    ('a', 'b', 'c')
    


```python
print(tuple(range(3)))
```

    (0, 1, 2)
    


```python
print(sorted((3, 1, 2)))
```

    [1, 2, 3]
    


```python
#Tuple Functions
```


```python
print(sum((1, 2, 3)))
```

    6
    


```python
print(min((1, 2, 3)))
```

    1
    


```python
print(max((1, 2, 3)))

```

    3
    


```python
print(all((1, True, 3)))

```

    True
    


```python
print(any((0, 0, 1)))

```

    True
    


```python
print(list((1, 2, 3)))
```

    [1, 2, 3]
    


```python
print(str((1, 2)))

```

    (1, 2)
    


```python
print(reversed((1, 2, 3)))

```

    <reversed object at 0x0000021F7A08B910>
    


```python
for i in reversed((1, 2, 3)):
    print(i)
```

    3
    2
    1
    


```python
print(tuple(reversed((1, 2, 3))))
```

    (3, 2, 1)
    


```python
#Tuple Unpacking
```


```python
a, b = (10, 20)
print(a, b)
```

    10 20
    


```python
a, b, c = (1, 2, 3)
print(c)
```

    3
    


```python
t = (1, 2, 3, 4)
a, *b = t
print(b)
```

    [2, 3, 4]
    


```python
*a, b = t
print(a, b)
```

    [1, 2, 3] 4
    


```python
a, b, *c = t
print(c)
```

    [3, 4]
    


```python
a, b, c, d = (10, 20, 30, 40)
print(f"{a=}, {b=}, {c=}, {d=}")
```

    a=10, b=20, c=30, d=40
    


```python
t1 = (1, 2)
t2 = (3, 4)
a, b, c, d = (*t1, *t2)
print(a + d)
```

    5
    


```python
x, y = divmod(10, 3)
print(x, y)


```

    3 1
    


```python
data = [(1, 2), (3, 4)]
for a, b in data:
    print(a + b)
```

    3
    7
    


```python
for idx, val in enumerate((10, 20, 30)):
    print(idx, val)

```

    0 10
    1 20
    2 30
    


```python
#Tuple Methods / Immutable Nature

```


```python
t = (1, 2, 3, 2)
print(t.count(2))
```

    2
    


```python
print(t.index(3))
```

    2
    


```python
try:
    t[0] = 100
except TypeError as e:
    print(e)
```

    'tuple' object does not support item assignment
    


```python
try:
    t.append(4)
except AttributeError as e:
    print(e)
```

    'tuple' object has no attribute 'append'
    


```python
x = (1, 2, 3)
print(id(x))
x = x + (4,)
print(id(x))  # different object

```

    2334221183360
    2334221131648
    


```python
t = (1, [2, 3])
t[1][0] = 99  # mutable inside
print(t)
```

    (1, [99, 3])
    


```python
t = (1, 2, 3)
print(t.index(2))
```

    1
    


```python
print((1, 2) == (1, 2))

```

    True
    


```python
print((1, 2) < (2, 1))
```

    True
    


```python
#Tuple with Other Data Types
```


```python
mixed = (1, "two", 3.0)
print(mixed)
```

    (1, 'two', 3.0)
    


```python
print(isinstance((1, 2), tuple))
```

    True
    


```python
d = {"a": 1, "b": 2}
print(tuple(d.items()))
```

    (('a', 1), ('b', 2))
    


```python
print(list(d.items()))
```

    [('a', 1), ('b', 2)]
    


```python
print(tuple(d.keys()))
```

    ('a', 'b')
    


```python
print(tuple(d.values()))
```

    (1, 2)
    


```python
names = ["a", "b"]
scores = [10, 20]
zipped = tuple(zip(names, scores))
print(zipped)
```

    (('a', 10), ('b', 20))
    


```python
unzipped = zip(*zipped)
print(tuple(unzipped))

```

    (('a', 'b'), (10, 20))
    


```python
args = (5, 2)
print(pow(*args))
```

    25
    


```python
matrix = ((1, 2), (3, 4))
for row in matrix:
    print(row)
```

    (1, 2)
    (3, 4)
    


```python
#Advanced / Tricks / Tuple Use Cases
```


```python
coords = ((0, 0), (1, 1))
for x, y in coords:
    print(x + y)
```

    0
    2
    


```python
for pair in [(1, 2), (3, 4)]:
    print(sum(pair))
```

    3
    7
    


```python
for pair in [(1, 2), (3, 4)]:
    print(sum(pair))
```

    3
    7
    


```python
def multi_return():
    return 1, 2, 3
x, y, z = multi_return()
print(z)
```

    3
    


```python
t = (4, 5, 6)
print("ID:", id(t))

```

    ID: 2334221288512
    


```python
print(hash((1, 2, 3)))
```

    529344067295497451
    


```python
print(tuple())
print(() == ())
```

    ()
    True
    


```python
print((1,) * 3)
```

    (1, 1, 1)
    


```python
print((0,) * 5)
```

    (0, 0, 0, 0, 0)
    


```python
nums = 1, 2, 3
print(sum(nums))
```

    6
    


```python
#Tuple Comprehension (via Generator)
```


```python
gen = (x**2 for x in range(3))
print(tuple(gen))

```

    (0, 1, 4)
    


```python
print(tuple(map(str, [1, 2, 3])))
```

    ('1', '2', '3')
    


```python
print(tuple(filter(lambda x: x > 1, [1, 2, 3])))
```

    (2, 3)
    


```python
t = tuple(i for i in range(5) if i % 2 == 0)
print(t)
```

    (0, 2, 4)
    


```python
names = ["Tom", "Tim"]
lengths = tuple(len(n) for n in names)
print(lengths)

```

    (3, 3)
    


```python
s = "abc"
print(tuple(enumerate(s)))
```

    ((0, 'a'), (1, 'b'), (2, 'c'))
    


```python
for i, c in enumerate("hi"):
    print(i, c)
```

    0 h
    1 i
    


```python
pairs = [("a", 1), ("b", 2)]
print(dict(pairs))
```

    {'a': 1, 'b': 2}
    


```python
print(tuple(dict(pairs).items()))
```

    (('a', 1), ('b', 2))
    


```python
t = tuple(zip("abc", range(3)))
print(t)
```

    (('a', 0), ('b', 1), ('c', 2))
    


```python
t = [(3, 'c'), (1, 'a'), (2, 'b')]
print(sorted(t))  # by first
```

    [(1, 'a'), (2, 'b'), (3, 'c')]
    


```python
print(sorted(t, key=lambda x: x[1]))  # by second

```

    [(1, 'a'), (2, 'b'), (3, 'c')]
    


```python
data = [("John", 90), ("Alice", 95)]
top = max(data, key=lambda x: x[1])
print(top)
```

    ('Alice', 95)
    


```python
points = [(0, 0), (1, 1), (2, 3)]
print([x for x, y in points])
```

    [0, 1, 2]
    


```python
flatten = ((1, 2), (3, 4))
print(sum(flatten, ()))  # flattening

```

    (1, 2, 3, 4)
    


```python
nested = ((1,), (2, 3), (4,))
for tup in nested:
    print(len(tup))
```

    1
    2
    1
    


```python
t = tuple(sorted([3, 1, 2]))
print(t)
```

    (1, 2, 3)
    


```python
print(tuple(reversed((1, 2, 3))))
```

    (3, 2, 1)
    


```python
seq = ((1, 2), (3, 4))
print(tuple(sum(seq, ())))

```

    (1, 2, 3, 4)
    


```python
print(len(set([(1, 2), (1, 2), (2, 3)])))

```

    2
    


```python
#Tuple Tricks / Enumerate / Internals
```


```python
print(any(isinstance(i, tuple) for i in [(1, 2), 3]))
```

    True
    


```python
print(all(isinstance(i, tuple) for i in [(1, 2), (3, 4)]))

```

    True
    


```python
seq = [(1, 2), (3, 4)]
flat = [x for tup in seq for x in tup]
print(flat)
```

    [1, 2, 3, 4]
    


```python
t = (None,) * 3
print(t)
```

    (None, None, None)
    


```python
data = (1, 2, 3)
x, y, z = data
print(x, y, z)
```

    1 2 3
    


```python
x = (1, 2)
a, b = x
print(a + b)
```

    3
    


```python
tuple_str = "(1, 2, 3)"
print(eval(tuple_str))

```

    (1, 2, 3)
    


```python
tpl = (i for i in range(3))
print(tuple(tpl))

```

    (0, 1, 2)
    


```python
tpl = (1, "two", [3, 4])
print(tpl[2][1])  # 4
```

    4
    


```python
nested = ((1, 2), (3, 4), (5, 6))
print(nested[1][0])  # Output: 3
```

    3
    


```python
t = ('a',) * 5
print(t)  # Output: ('a', 'a', 'a', 'a', 'a')
```

    ('a', 'a', 'a', 'a', 'a')
    


```python
a = (1, 2)
b = [3, 4]
combined = (*a, *b)
print(combined)  # Output: (1, 2, 3, 4)

```

    (1, 2, 3, 4)
    


```python
mixed = (1, 'two', 3.0, [4, 5])
print(mixed)

```

    (1, 'two', 3.0, [4, 5])
    


```python
tup = ('a', 'b', 'c')
for index, value in enumerate(tup):
    print(index, value)

```

    0 a
    1 b
    2 c
    


```python
words = ('Hello', 'World')
sentence = ' '.join(words)
print(sentence)  # Output: Hello World

```

    Hello World
    


```python
t = (1, 2, 3, 4)
print(t[::-1])  # Output: (4, 3, 2, 1)

```

    (4, 3, 2, 1)
    


```python
nested = ((1, 2), (3, 4))
flat = tuple(i for t in nested for i in t)
print(flat)  # Output: (1, 2, 3, 4)

```

    (1, 2, 3, 4)
    


```python
a = (1, 2, 3)
b = ('a', 'b', 'c')
zipped = tuple(zip(a, b))
print(zipped)  # Output: ((1, 'a'), (2, 'b'), (3, 'c'))

```

    ((1, 'a'), (2, 'b'), (3, 'c'))
    


```python
pairs = [(1, 'one'), (2, 'two')]
for num, name in pairs:
    print(num, name)

```

    1 one
    2 two
    


```python
d = {'a': 1, 'b': 2}
print(tuple(d))  # Output: ('a', 'b')

```

    ('a', 'b')
    


```python
nums = (5, 2, 9, 1)
print(min(nums), max(nums))  # Output: 1 9

```

    1 9
    


```python
data = [(1, 2), (1, 2), (2, 3)]
unique = set(data)
print(unique)  # Output: {(1, 2), (2, 3)}

```

    {(2, 3), (1, 2)}
    


```python
colors = ('red', 'green', 'blue')
print('green' in colors)  # Output: True

```

    True
    


```python
a, b = 10, 20
a, b = b, a
print(a, b)  # Output: 20 10

```

    20 10
    


```python
my_dict = {('x', 1): 'value'}
print(my_dict[('x', 1)])  # Output: value

```

    value
    


```python
t = (1, 2, 3, 4)
a, *b = t
print(a, b)  # Output: 1 [2, 3, 4]

```

    1 [2, 3, 4]
    


```python
squares = tuple(x*x for x in range(5))
print(squares)  # Output: (0, 1, 4, 9, 16)

```

    (0, 1, 4, 9, 16)
    


```python
from collections import Counter
t = ('a', 'b', 'a', 'c', 'b')
print(Counter(t))  # Output: Counter({'a': 2, 'b': 2, 'c': 1})

```

    Counter({'a': 2, 'b': 2, 'c': 1})
    


```python
lst = [('a', 1), ('b', 2)]
d = dict(lst)
print(d)  # Output: {'a': 1, 'b': 2}

```

    {'a': 1, 'b': 2}
    


```python

```


---
**Score: 125**