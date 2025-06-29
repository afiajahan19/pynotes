---
title: Built-In-Functions
date: 2025-06-29
author: Your Name
cell_count: 123
score: 120
---

```python
#tuples
```


```python
t = (1, 2, 3)
print(len(t))
```

    3
    


```python
print(max((4, 7, 2)))
```

    7
    


```python
print(min((4, 7, 2)))
```

    2
    


```python
print(sum((10, 20, 30)))
```

    60
    


```python
print(any((0, 0, 1)))
```

    True
    


```python
print(all((1, 1, 1)))

```

    True
    


```python
print(tuple([1, 2, 3]))

```

    (1, 2, 3)
    


```python
print(sorted((5, 1, 3)))
```

    [1, 3, 5]
    


```python
print((1, 2, 1, 3).count(1))

```

    2
    


```python
print((5, 2, 3).index(2))
```

    1
    


```python
print(type((1, 2)))
```

    <class 'tuple'>
    


```python
a = (1, 2)
b = (3, 4)
print(list(zip(a, b)))
```

    [(1, 3), (2, 4)]
    


```python
print(tuple(reversed((1, 2, 3))))
```

    (3, 2, 1)
    


```python
for i, v in enumerate(('a', 'b')):
    print(i, v)

```

    0 a
    1 b
    


```python
print(3 in (1, 2, 3))

```

    True
    


```python
print(4 not in (1, 2, 3))
```

    True
    


```python
print(tuple(map(str, (1, 2, 3))))
```

    ('1', '2', '3')
    


```python
print(tuple(filter(lambda x: x > 1, (0, 1, 2, 3))))

```

    (2, 3)
    


```python
print(isinstance((1, 2), tuple))
```

    True
    


```python
print(id((1, 2)))
```

    1883265549120
    


```python
#sets
```


```python
print(len({1, 2, 3}))

```

    3
    


```python
s = {1, 2}
s.add(3)
print(s)

```

    {1, 2, 3}
    


```python
s.remove(2)
print(s)
```

    {1, 3}
    


```python
s.discard(10)
print(s)

```

    {1, 3}
    


```python
print(s.pop())
```

    1
    


```python
s.clear()
print(s)

```

    set()
    


```python
print(set([1, 2, 3]))
```

    {1, 2, 3}
    


```python
print({1, 2}.union({2, 3}))
```

    {1, 2, 3}
    


```python
print({1, 2}.intersection({2, 3}))

```

    {2}
    


```python
print({1, 2, 3}.difference({2}))

```

    {1, 3}
    


```python
print({1, 2}.symmetric_difference({2, 3}))
```

    {1, 3}
    


```python
print({1}.issubset({1, 2}))
```

    True
    


```python
print({1, 2}.issuperset({1}))

```

    True
    


```python
print({1, 2}.isdisjoint({3}))

```

    True
    


```python
a = {1, 2}
b = a.copy()
print(b)

```

    {1, 2}
    


```python
f = frozenset([1, 2, 3])
print(f)

```

    frozenset({1, 2, 3})
    


```python
print(sorted({3, 1, 2}))
```

    [1, 2, 3]
    


```python
print(2 in {1, 2, 3})
```

    True
    


```python
print(4 not in {1, 2, 3})
```

    True
    


```python
print(sum({1, 2, 3}))
```

    6
    


```python
#strings
```


```python
print(len("hello"))
```

    5
    


```python
print("abc".upper())

```

    ABC
    


```python
print("ABC".lower())
```

    abc
    


```python
print("hello".capitalize())
```

    Hello
    


```python
print("hello world".title())

```

    Hello World
    


```python
print("HeLLo".swapcase())
```

    hEllO
    


```python
print("  hi  ".strip())
```

    hi
    


```python
print("hi  ".rstrip())
```

    hi
    


```python
print("hello hello".rfind("l"))
```

    9
    


```python
print("hello".replace("l", "x"))
```

    hexxo
    


```python
print("a,b,c".split(","))
```

    ['a', 'b', 'c']
    


```python
print("a b c".rsplit())
```

    ['a', 'b', 'c']
    


```python
print("-".join(["a", "b", "c"]))
```

    a-b-c
    


```python
print("banana".count("a"))
```

    3
    


```python
print("abc".isalpha())
```

    True
    


```python
print("123".isdigit())
```

    True
    


```python
print("123".isnumeric())
```

    True
    


```python
print("abc123".isalnum())
```

    True
    


```python
print("abc".islower())
```

    True
    


```python
print("ABC".isupper())
```

    True
    


```python
print("python".startswith("py"))
```

    True
    


```python
print("main.py".endswith(".py"))
```

    True
    


```python
print("abc".encode())
```

    b'abc'
    


```python
print("Hello {}".format("World"))
```

    Hello World
    


```python
print("{x} + {y}".format_map({'x': 1, 'y': 2}))
```

    1 + 2
    


```python
print("a=b".partition("="))
```

    ('a', '=', 'b')
    


```python
print("a=b=c".rpartition("="))
```

    ('a=b', '=', 'c')
    


```python
print("a\tb".expandtabs(4))
```

    a   b
    


```python
print(" ".isspace())
```

    True
    


```python
print("Hello World".istitle())
```

    True
    


```python
print("42".zfill(5))
```

    00042
    


```python
print("hi".ljust(5, '-'))
```

    hi---
    


```python
print("hi".rjust(5, '-'))
```

    ---hi
    


```python
print("hi".center(6, '*'))
```

    **hi**
    


```python
print("HELLO".casefold())
```

    hello
    


```python
table = str.maketrans("ae", "12")
print("apple".translate(table))

```

    1ppl2
    


```python
print(str.maketrans("abc", "123"))
```

    {97: 49, 98: 50, 99: 51}
    


```python
#dictionary
```


```python
d = {"a": 1, "b": 2}
print(len(d))

```

    2
    


```python
print(d.keys())
```

    dict_keys(['a', 'b'])
    


```python
print(d.values())

```

    dict_values([1, 2])
    


```python
print(d.items())
```

    dict_items([('a', 1), ('b', 2)])
    


```python
print(d.get("a"))
```

    1
    


```python
print(d.popitem())
```

    ('b', 2)
    


```python
d.update({"c": 3})
print(d)
```

    {'c': 3}
    


```python
d.clear()
print(d)
```

    {}
    


```python
print(dict.fromkeys(['x', 'y'], 0))
```

    {'x': 0, 'y': 0}
    


```python
d = {'a': 1}
print(d.setdefault('b', 2))
```

    2
    


```python
print("a" in {'a': 1})
```

    True
    


```python
print("x" not in {'a': 1})
```

    True
    


```python
d = {'a': 1}
del d['a']
print(d)
```

    {}
    


```python
print(dict(name="John", age=25))
```

    {'name': 'John', 'age': 25}
    


```python
a = {'x': 10}
b = a.copy()
print(b)
```

    {'x': 10}
    


```python
print(dict(zip(['a', 'b'], [1, 2])))
```

    {'a': 1, 'b': 2}
    


```python
print(sorted({'b': 2, 'a': 1}))
```

    ['a', 'b']
    


```python
print(max({'x': 1, 'y': 3}))
```

    y
    


```python
d = {'a': 4, 'b': 1}
print(min(d.values()))
```

    1
    


```python
#files
```


```python
with open("test.txt", "w") as f:
    f.write("Hello")

```


```python
with open("test.txt", "r") as f:
    print(f.read())

```

    Hello
    


```python
with open("test.txt", "r") as f:
    print(f.readline())
```

    Hello
    


```python
with open("test.txt", "r") as f:
    print(f.readlines())
```

    ['Hello']
    


```python
lines = ["Line1\n", "Line2\n"]
with open("test2.txt", "w") as f:
    f.writelines(lines)
```


```python
with open("test2.txt", "r") as f:
    print(f.tell())

```

    0
    


```python
with open("test2.txt", "r") as f:
    f.seek(0)
    print(f.read(5))
```

    Line1
    


```python
f = open("test.txt", "r")
f.close()
```


```python
with open("test.txt", "r") as f:
    pass
```


```python
with open("test.txt", "r") as f:
    print(f.mode)
```

    r
    


```python
with open("test.txt", "r") as f:
    print(f.name)
```

    test.txt
    


```python
with open("test.txt", "r") as f:
    print(f.readable())
```

    True
    


```python
with open("test.txt", "r") as f:
    print(f.readable())
```

    True
    


```python
with open("test.txt", "r") as f:
    print(f.writable())
```

    False
    


```python
with open("test.txt", "r") as f:
    print(f.seekable())
```

    True
    


```python
with open("test.txt", "a") as f:
    f.truncate(5)
```


```python
with open("test.txt", "r") as f:
    print(f.encoding)

```

    cp1252
    


```python
with open("test.txt", "w") as f:
    f.write("flush")
    f.flush()
```


```python
with open("test.txt", "rb") as f:
    print(f.read())

```

    b'flush'
    


```python
with open("test.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

    flush
    


```python
try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")
```

    File not found!
    


```python

```


---
**Score: 120**