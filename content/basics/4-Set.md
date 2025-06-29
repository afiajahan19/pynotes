---
title: 4-Set
date: 2025-06-29
author: Your Name
cell_count: 159
score: 155
---

```python
s = {1, 2, 3}
```


```python
print(s)
```

    {1, 2, 3}
    


```python
print(len(s)) 
```

    3
    


```python
print(2 in s)
```

    True
    


```python
print(2 in s)
```

    True
    


```python
s.add(4)
```


```python
print(s)
```

    {1, 2, 3, 4}
    


```python
s.remove(3)
```


```python
print(s)
```

    {1, 2, 4}
    


```python
s.discard(5)
```


```python
print(s)
```

    {1, 2, 4}
    


```python
s.update([5, 6])
```


```python
print(s)
```

    {1, 2, 3}
    


```python
s.clear()
```


```python
print(s)
```

    {1, 2, 3}
    


```python
s = set([1, 2, 3])
```


```python
print(s)
```

    {1, 2, 3}
    


```python
print(set("hello"))
```

    {'o', 'l', 'h', 'e'}
    


```python
a = {1, 2, 3}
b = {3, 4, 5}
```


```python
#union
```


```python
print(a | b)  
```

    {1, 2, 3, 4, 5}
    


```python
#intersection
```


```python
print(a & b)  
```

    {3}
    


```python
# difference
```


```python
print(a - b) 
```

    {1, 2}
    


```python
print(b - a) 
```

    {4, 5}
    


```python
# symmetric difference
```


```python
print(a ^ b) 
```

    {1, 2, 4, 5}
    


```python
print(a.union(b))
```

    {1, 2, 3, 4, 5}
    


```python
print(a.intersection(b))
```

    {3}
    


```python
print(a.difference(b))
```

    {1, 2}
    


```python
print(a.symmetric_difference(b))
```

    {1, 2, 4, 5}
    


```python
a |= b
```


```python
print(a)
```

    {1, 2, 4, 5}
    


```python
a = {1, 2, 3}
a &= b
```


```python
print(a)
```

    {3}
    


```python
a = {1, 2, 3}
a -= b
```


```python
print(a)
```

    {1, 2}
    


```python
a = {1, 2, 3}
a ^= b
```


```python
print(a)
```

    {1, 2, 4, 5}
    


```python
print(a.isdisjoint(b))
```

    False
    


```python
print(a.issubset(b))
```

    False
    


```python
print(a.issuperset(b))
```

    False
    


```python
a = {1, 2}
b = {1, 2, 3}
```


```python
print(a < b) 
```

    True
    


```python
print(b > a)
```

    True
    


```python
print(bool(set()))
```

    False
    


```python
print(set(range(5)))

```

    {0, 1, 2, 3, 4}
    


```python
s = {1, 2, 3}
```


```python
for i in s:
    print(i)
```

    1
    2
    3
    


```python
s1 = {1, 2, 3}
s2 = s1.copy()
```


```python
print(s2)

```

    {1, 2, 3}
    


```python
print(s1 is s2)
```

    False
    


```python
print(s1 == s2) 
```

    True
    


```python
s = {1, 2, 2, 3}
```


```python
print(s)
```

    {1, 2, 3}
    


```python
print(len({1, 2, 2, 3}))
```

    3
    


```python
print(set([1, 2, 2, 3]))
```

    {1, 2, 3}
    


```python
a = {1, 2, 3}
b = {2, 3}
```


```python
print(b <= a)
```

    True
    


```python
print(a >= b) 
```

    True
    


```python
print({x for x in range(10) if x % 2 == 0})
```

    {0, 2, 4, 6, 8}
    


```python
print(set("banana")) 
```

    {'n', 'b', 'a'}
    


```python
print({x.upper() for x in "abc"})
```

    {'B', 'A', 'C'}
    


```python
s = {1, 2, 3}
s2 = frozenset(s)
```


```python
print(s2)
```

    frozenset({1, 2, 3})
    


```python
print(type(s))
```

    <class 'set'>
    


```python
s = set()
s.add(1)
```


```python
print(s)
```

    {1}
    


```python
print(set()) 
```

    set()
    


```python
print({})
```

    {}
    


```python
print({1, 2}.union([3, 4]))
```

    {1, 2, 3, 4}
    


```python
print({1, 2}.intersection([2, 3]))
```

    {2}
    


```python
print({1, 2}.difference([2]))
```

    {1}
    


```python
print({1, 2}.symmetric_difference([2, 3]))
```

    {1, 3}
    


```python
print(set("abc") & set("bcd"))
```

    {'b', 'c'}
    


```python
print(set("abc") | set("bcd"))
```

    {'b', 'a', 'd', 'c'}
    


```python
print(set("abc") - set("bcd"))
```

    {'a'}
    


```python
print(set("abc") ^ set("bcd"))
```

    {'a', 'd'}
    


```python
x = {1, 2}
```


```python
print(all(i < 3 for i in x))
```

    True
    


```python
print(any(i > 1 for i in x))
```

    True
    


```python
print(max(x), min(x))
```

    2 1
    


```python
print(sum(x))
```

    3
    


```python
print(sorted(x))
```

    [1, 2]
    


```python
print(sorted(set("banana")))
```

    ['a', 'b', 'n']
    


```python
print(len(set("mississippi")))
```

    4
    


```python
s = set("hello")
```


```python
print("h" in s)
```

    True
    


```python
print("z" not in s)
```

    True
    


```python
s = {x**2 for x in range(5)}
```


```python
print(s)
```

    {0, 1, 4, 9, 16}
    


```python
print(set(range(5)) & set(range(3, 8)))
```

    {3, 4}
    


```python
print(set(range(5)) - set(range(3, 8)))
```

    {0, 1, 2}
    


```python
print(set(range(5)) ^ set(range(3, 8)))
```

    {0, 1, 2, 5, 6, 7}
    


```python
a = {1, 2}
b = a
```


```python
a.add(3)
```


```python
print(b)
```

    {1, 2, 3}
    


```python
a = {1, 2}
```


```python
b = a.copy()
```


```python
a.add(3)
```


```python
print(b) 
```

    {1, 2}
    


```python
print(hash(frozenset([1, 2])))
```

    -1826646154956904602
    


```python
fs = frozenset("hello")

```


```python
print("e" in fs)
```

    True
    


```python
print(fs.isdisjoint({"x", "y"}))
```

    True
    


```python
fs2 = frozenset("help")
```


```python
print(fs & fs2)
```

    frozenset({'l', 'h', 'e'})
    


```python
print(fs | fs2)

```

    frozenset({'o', 'p', 'l', 'h', 'e'})
    


```python
print(fs - fs2)
```

    frozenset({'o'})
    


```python
print(fs ^ fs2)
```

    frozenset({'o', 'p'})
    


```python
a = set("python")
```


```python
print([ch for ch in a])
```

    ['o', 'p', 'h', 't', 'y', 'n']
    


```python
print({i for i in range(10) if i % 3 == 0})
```

    {0, 9, 3, 6}
    


```python
s = set([None, False, 0, "", 1])
```


```python
print(s)
```

    {None, False, '', 1}
    


```python
print(set([1, 2, 3]) == set([3, 2, 1]))
```

    True
    


```python
print(set("abc").intersection("cba"))
```

    {'b', 'a', 'c'}
    


```python
print(set("abc").issubset("abcd"))
```

    True
    


```python
print(set("abcd").issuperset("abc"))
```

    True
    


```python
print(set("abc").isdisjoint("xyz"))
```

    True
    


```python
x = {"a", "b"}
```


```python
y = {"c", "d"}
```


```python
z = {"b", "c"}
```


```python
print(x.isdisjoint(y)) 
```

    True
    


```python
print(x.isdisjoint(z)) 
```

    False
    


```python
print(set(map(int, ["1", "2", "2"])))
```

    {1, 2}
    


```python
print(set(filter(lambda x: x % 2 == 0, range(10))))
```

    {0, 2, 4, 6, 8}
    


```python
print(set(i for i in range(5) if i % 2))
```

    {1, 3}
    


```python
print(set(zip([1, 2], [3, 4])))
```

    {(2, 4), (1, 3)}
    


```python
print(set(i*i for i in range(5)))
```

    {0, 1, 4, 9, 16}
    


```python
print(set(i for i in range(5)).issubset(range(10)))
```

    True
    


```python
print(set("abc").union("def"))
```

    {'f', 'c', 'b', 'a', 'd', 'e'}
    


```python
print(set("abcdef") - set("ace"))
```

    {'b', 'f', 'd'}
    


```python
print(set(chr(i) for i in range(65, 70)))
```

    {'A', 'B', 'C', 'D', 'E'}
    


```python
print(set().union([1, 2], [2, 3]))
```

    {1, 2, 3}
    


```python
print(set().intersection([1, 2], [2, 3]))
```

    set()
    


```python
print(set().difference([1, 2], [2, 3]))
```

    set()
    


```python
a = {1, 2, 3}
for val in a.copy():
    if val % 2 == 0:
        a.remove(val)
print(a)

```

    {1, 3}
    


```python
a = set("banana")
for ch in "ban":
    a.discard(ch)
print(a)
```

    set()
    


```python
print({1, 2} == set([2, 1]))
```

    True
    


```python
print({1, 2}.issuperset({1}))
```

    True
    


```python
print({1}.issubset({1, 2}))
```

    True
    


```python
print(set(range(3)).intersection(range(5)))
```

    {0, 1, 2}
    


```python
print(set(range(5)).difference(range(3)))
```

    {3, 4}
    


```python
print(set(range(5)).symmetric_difference(range(3)))
```

    {3, 4}
    


```python
print({i for i in range(10) if i not in {1, 3, 5}})
```

    {0, 2, 4, 6, 7, 8, 9}
    


```python
print(set(i for i in range(3)).union([3, 4]))
```

    {0, 1, 2, 3, 4}
    


```python
print(set(i for i in range(3)).difference({1}))

```

    {0, 2}
    


```python
print(set(i for i in range(3)).symmetric_difference({2}))
```

    {0, 1}
    


```python
print(set("a b c".split()))
```

    {'b', 'a', 'c'}
    


```python
print(set("a,b,c".split(",")))
```

    {'b', 'a', 'c'}
    


```python
print(set("123") & set("345"))
```

    {'3'}
    


```python
print(set(["apple", "banana", "apple"]))
```

    {'apple', 'banana'}
    


```python
words = {"python", "java", "c"}
print({w.upper() for w in words})
```

    {'JAVA', 'C', 'PYTHON'}
    


```python
print({x for x in range(5)} == {0, 1, 2, 3, 4})
```

    True
    


```python
print(set("Hello".lower()) == set("hello"))
```

    True
    


```python
print({i for i in range(100) if str(i).endswith("5")})
```

    {65, 35, 5, 75, 45, 15, 85, 55, 25, 95}
    


```python

```


---
**Score: 155**