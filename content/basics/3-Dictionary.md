---
title: 3-Dictionary
date: 2025-06-29
author: Your Name
cell_count: 179
score: 175
---

```python
d = {"a": 1, "b": 2}
```


```python
print(d)

```

    {'a': 1, 'b': 2}
    


```python
print(len(d))
```

    2
    


```python
print(d["a"])
```

    1
    


```python
d["c"] = 3
```


```python
print(d)
```

    {'a': 1, 'b': 2, 'c': 3}
    


```python
d["a"] = 10
```


```python
print(d)
```

    {'a': 10, 'b': 2, 'c': 3}
    


```python
del d["b"]
```


```python
print(d)
```

    {'a': 10, 'c': 3}
    


```python
print("a" in d) 
```

    True
    


```python
print("z" in d) 
```

    False
    


```python
print(d.get("a"))  
```

    10
    


```python
print(d.get("z")) 
```

    None
    


```python
print(d.get("z", 0))
```

    0
    


```python
print(d.keys())
```

    dict_keys(['a', 'c'])
    


```python
print(d.values())
```

    dict_values([10, 3])
    


```python
print(d.items())
```

    dict_items([('a', 10), ('c', 3)])
    


```python
for key in d:
    print(key)
```

    a
    c
    


```python
for val in d.values():
    print(val)
```

    10
    3
    


```python
for k, v in d.items():
    print(k, v)
```

    a 10
    c 3
    


```python
d.clear()

```


```python
print(d)
```

    {}
    


```python
d = dict(a=1, b=2)


```


```python
print(d)
```

    {'a': 1, 'b': 2}
    


```python
d2 = dict([("x", 9), ("y", 8)])

```


```python
print(d2)
```

    {'x': 9, 'y': 8}
    


```python
d3 = {"one": 1, "two": 2}

```


```python
print(d3.pop("one"))
```

    1
    


```python
print(d3)
```

    {'two': 2}
    


```python
d3["three"] = 3

```


```python
print(d3.popitem())
```

    ('three', 3)
    


```python
d4 = {"a": 1}
```


```python
d4.update({"b": 2})
```


```python
print(d4)
```

    {'a': 1, 'b': 2}
    


```python
d4.update(c=3)
```


```python
print(d4)

```

    {'a': 1, 'b': 2, 'c': 3}
    


```python
d4.update([("d", 4)])
```


```python
print(d4)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    


```python
d5 = d4.copy()
```


```python
print(d5)
```

    {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    


```python
print(d5 is d4)
```

    False
    


```python
d5["a"] = 100
```


```python
print(d4["a"]) 
```

    1
    


```python
defaults = {"x": 0, "y": 0}
```


```python
print(defaults.setdefault("x", 5)) 
```

    0
    


```python
print(defaults.setdefault("z", 9))
```

    9
    


```python
print(defaults)
```

    {'x': 0, 'y': 0, 'z': 9}
    


```python
print({x: x**2 for x in range(3)})
```

    {0: 0, 1: 1, 2: 4}
    


```python
names = ["a", "b"]


```


```python
scores = [10, 20]
```


```python
print(dict(zip(names, scores)))
```

    {'a': 10, 'b': 20}
    


```python
print(dict.fromkeys(["a", "b", "c"], 0))
```

    {'a': 0, 'b': 0, 'c': 0}
    


```python
for i in dict.fromkeys("abc"):
    print(i)
```

    a
    b
    c
    


```python
d = {"a": 1}


```


```python
print("a" in d)
```

    True
    


```python
print("z" not in d)
```

    True
    


```python
d = {"x": 1}
```


```python
d["x"] += 1
```


```python
print(d)
```

    {'x': 2}
    


```python
print(type(d))
```

    <class 'dict'>
    


```python
print(list(d))
```

    []
    


```python
print(list(d.items()))
```

    []
    


```python
print(sorted(d)) 
```

    []
    


```python
d = {"a": 1, "b": {"c": 2}}
```


```python
print(d["b"]["c"])
```

    2
    


```python
d = {"a": 1, "b": 2}
```


```python
d2 = {"b": 3, "c": 4}
```


```python
d.update(d2)
```


```python
print(d)
```

    {'a': 1, 'b': 3, 'c': 4}
    


```python
print({k:v for k,v in d.items() if v > 2})
```

    {'b': 3, 'c': 4}
    


```python
print({v:k for k,v in d.items()})
```

    {1: 'a', 3: 'b', 4: 'c'}
    


```python
nested = {"outer": {"inner": 1}}
```


```python
print(nested["outer"]["inner"])
```

    1
    


```python
d = {}
```


```python
d["new"] = d.get("new", 0) + 1
```


```python
print(d)
```

    {'new': 1}
    


```python
freq = {}

```


```python
for ch in "banana":
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
```

    {'b': 1, 'a': 3, 'n': 2}
    


```python
data = [("a", 1), ("b", 2)]
```


```python
d = dict(data)
```


```python
print(d)
```

    {'a': 1, 'b': 2}
    


```python
print({k:len(k) for k in ["apple", "banana"]})
```

    {'apple': 5, 'banana': 6}
    


```python
print({i:chr(i) for i in range(65, 70)})
```

    {65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E'}
    


```python
print({chr(i):i for i in range(65, 70)})
```

    {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69}
    


```python
pairs = ["a=1", "b=2"]

```


```python
print({p.split("=")[0]: int(p.split("=")[1]) for p in pairs})
```

    {'a': 1, 'b': 2}
    


```python
print(all(k in d for k in ["a", "b"]))

```

    True
    


```python
print(any(v == 2 for v in d.values()))

```

    True
    


```python
print(sum(d.values()))
```

    3
    


```python
print(min(d.values()))
```

    1
    


```python
print(max(d.values()))
```

    2
    


```python
print(len(d.keys()) == len(set(d.keys())))

```

    True
    


```python
data = {"a": 10, "b": 20}
```


```python
print({k: v*2 for k, v in data.items()})
```

    {'a': 20, 'b': 40}
    


```python
d = {"x": 10}
```


```python
print(d.get("y", "not found"))
```

    not found
    


```python
d = dict()
```


```python
print(bool(d)) 
```

    False
    


```python
print(dict(a=1, b=2) == {"a": 1, "b": 2})
```

    True
    


```python
x = {"a": 1, "b": 2}
```


```python
y = {"b": 3, "c": 4}
```


```python
z = {**x, **y}
```


```python
print(z) 
```

    {'a': 1, 'b': 3, 'c': 4}
    


```python
d = {"a": 1, "b": 2}
```


```python
print(hash(frozenset(d.items())))
```

    -8457517723523400311
    


```python
print(list(d))
```

    ['a', 'b']
    


```python
print(list(d.values()))

```

    [1, 2]
    


```python
print({k: v for k, v in d.items() if k != "b"})
```

    {'a': 1}
    


```python
from collections import defaultdict
dd = defaultdict(int)
dd["a"] += 1
print(dd)
```

    defaultdict(<class 'int'>, {'a': 1})
    


```python
dd = defaultdict(list)
dd["x"].append(10)
print(dd)

```

    defaultdict(<class 'list'>, {'x': [10]})
    


```python
from collections import OrderedDict
od = OrderedDict()
od["a"] = 1
od["b"] = 2
print(od)
```

    OrderedDict({'a': 1, 'b': 2})
    


```python
od.move_to_end("a")
print(od)

```

    OrderedDict({'b': 2, 'a': 1})
    


```python
from collections import Counter
c = Counter("mississippi")
print(c)
```

    Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
    


```python
print(c.most_common(2))
```

    [('i', 4), ('s', 4)]
    


```python
c.update("i")
print(c)

```

    Counter({'i': 5, 's': 4, 'p': 2, 'm': 1})
    


```python
c.update("i")
print(c)

```

    Counter({'i': 6, 's': 4, 'p': 2, 'm': 1})
    


```python
print(c["s"])
```

    4
    


```python
print(c.items())
```

    dict_items([('m', 1), ('i', 6), ('s', 4), ('p', 2)])
    


```python
c2 = Counter("miss")
```


```python
print(c + c2)
```

    Counter({'i': 7, 's': 6, 'm': 2, 'p': 2})
    


```python
print(c - c2)
```

    Counter({'i': 5, 's': 2, 'p': 2})
    


```python
print(c & c2)
```

    Counter({'s': 2, 'm': 1, 'i': 1})
    


```python
print(c | c2)
```

    Counter({'i': 6, 's': 4, 'p': 2, 'm': 1})
    


```python
print(dict(sorted(c.items(), key=lambda x: -x[1])))
```

    {'i': 6, 's': 4, 'p': 2, 'm': 1}
    


```python
d = {"x": [1, 2], "y": [3]}
```


```python
print(d["x"][1])
```

    2
    


```python
d["z"] = []
```


```python
d["z"].append(99)
```


```python
print(d)
```

    {'x': [1, 2], 'y': [3], 'z': [99]}
    


```python
d.setdefault("k", []).append(1)
```


```python
print(d)
```

    {'x': [1, 2], 'y': [3], 'z': [99], 'k': [1]}
    


```python
print(isinstance(d, dict))
```

    True
    


```python
nested = {"x": {"y": {"z": 1}}}
```


```python
print(nested["x"]["y"]["z"])
```

    1
    


```python
flat = {f"{k1}_{k2}": v for k1, inner in nested.items() for k2, v in inner["y"].items()}
```


```python
print(flat)
```

    {'x_z': 1}
    


```python
print({x: x % 2 == 0 for x in range(5)})
```

    {0: True, 1: False, 2: True, 3: False, 4: True}
    


```python
d = {"a": None}
```


```python
print(d.get("a") is None)
```

    True
    


```python
print({i: i**0.5 for i in range(1, 6)})
```

    {1: 1.0, 2: 1.4142135623730951, 3: 1.7320508075688772, 4: 2.0, 5: 2.23606797749979}
    


```python
print({k: v for k, v in zip("abc", range(3))})
```

    {'a': 0, 'b': 1, 'c': 2}
    


```python
data = ["a", "b", "c"]
```


```python
print(dict.fromkeys(data, 0))
```

    {'a': 0, 'b': 0, 'c': 0}
    


```python
print({x: bool(x % 2) for x in range(6)})
```

    {0: False, 1: True, 2: False, 3: True, 4: False, 5: True}
    


```python
a = {"one": 1}
```


```python
b = {"two": 2}
```


```python
merged = a | b
```


```python
print(merged)
```

    {'one': 1, 'two': 2}
    


```python
a |= {"three": 3}
```


```python
print(a)
```

    {'one': 1, 'three': 3}
    


```python
a.update(four=4)
```


```python
print(a)
```

    {'one': 1, 'three': 3, 'four': 4}
    


```python
d = {"x": 1}
```


```python
print(d.pop("x", "missing"))
```

    1
    


```python
print(d.pop("x", "missing")) 
```

    missing
    


```python
d = {"x": 1, "y": 2}
```


```python
print([*d])
```

    ['x', 'y']
    


```python
print({**{"a": 1}, **{"b": 2}})
```

    {'a': 1, 'b': 2}
    


```python
from types import MappingProxyType
read_only = MappingProxyType(d)
print(read_only["y"])
```

    2
    


```python
keys = "abc"
```


```python
vals = range(3)
```


```python
print(dict(zip(keys, vals)))
```

    {'a': 0, 'b': 1, 'c': 2}
    


```python
k, v = list(d.items())[0]
```


```python
print(k, v)
```

    x 1
    


```python
print(list(d.values())[0])
```

    1
    


```python
print(len(set(d.values())))
```

    2
    


```python
print(any(k.startswith("x") for k in d))
```

    True
    


```python
print({k: v for k, v in d.items() if k != "x"})
```

    {'y': 2}
    


```python
print({k.upper(): v for k, v in d.items()})
```

    {'X': 1, 'Y': 2}
    


```python
print({k: v for k, v in d.items() if isinstance(v, int)})
```

    {'x': 1, 'y': 2}
    


```python
print(all(isinstance(k, str) for k in d))
```

    True
    


```python
print({k: v for k, v in zip("abc", [1, 2, 3]) if v % 2})
```

    {'a': 1, 'c': 3}
    


```python
print({k: v for k, v in enumerate("xyz")})
```

    {0: 'x', 1: 'y', 2: 'z'}
    


```python
d = {"a": [1, 2], "b": [3, 4]}
```


```python
print(sum(sum(v) for v in d.values()))
```

    10
    


```python
print({k: v[::-1] for k, v in d.items()})
```

    {'a': [2, 1], 'b': [4, 3]}
    


```python
print({k: sum(v) for k, v in d.items()})
```

    {'a': 3, 'b': 7}
    


```python

```


---
**Score: 175**