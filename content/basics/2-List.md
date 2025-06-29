---
title: 2-List
date: 2025-06-29
author: Your Name
cell_count: 141
score: 140
---

```python
list = [
    "AB", 
    "CD",
    "EF",
    "GH",
    "IJ", 
    "KL",
    "MN",
    "OP",
    "QR",
    "ST",
    "UV",
    "WX",
    "YZ"
]
```


```python
list
```




    ['AB', 'CD', 'EF', 'GH', 'IJ', 'KL', 'MN', 'OP', 'QR', 'ST', 'UV', 'WX', 'YZ']




```python
# append to list
list.append("ABC")
```


```python
list
```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC']




```python
list.extend(["EFG", "IJK", "LMN"])
```


```python
list
```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN']




```python
list.extend(("OPQ", "RST"))
```


```python
list
```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST']




```python
list.extend(range(1, 5))
```


```python
list
```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4]




```python
list2 = ["One", "Two"]
```


```python
list2
```




    ['One', 'Two']




```python
list.append(list2)
```


```python
list

```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     ['One', 'Two']]




```python
list3 = ["Four", "Five"]
```


```python
list += list3
```


```python
list
```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     ['One', 'Two'],
     'Four',
     'Five']




```python
list.pop(len(list)-1)
```




    'Five'




```python
list
```




    ['AB',
     'CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     ['One', 'Two'],
     'Four']




```python
list.remove('AB')
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     ['One', 'Two'],
     'Four']




```python
list.remove(list2)
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four']




```python
list.extend(("ten", "twenty"))
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'ten',
     'twenty']




```python
list.extend(["eleven", "twelve"])
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'ten',
     'twenty',
     'eleven',
     'twelve']




```python
list.append(("six", "seven"))
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'ten',
     'twenty',
     'eleven',
     'twelve',
     ('six', 'seven')]




```python
type(list[len(list)-1])
```




    tuple




```python
del list[len(list)-1]
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'ten',
     'twenty',
     'eleven',
     'twelve']




```python
list.remove("ten")
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'twenty',
     'eleven',
     'twelve']




```python
list.append( ["one", "two"])
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'twenty',
     'eleven',
     'twelve',
     ['one', 'two']]




```python
list.remove(['one', 'two'])
```


```python
list
```




    ['CD',
     'EF',
     'GH',
     'IJ',
     'KL',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'twenty',
     'eleven',
     'twelve']




```python
# delete elements 1 - 5
del list[1:5]
```


```python
list
```




    ['CD',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'twenty',
     'eleven',
     'twelve']




```python
list[::2]
```




    ['CD', 'OP', 'ST', 'WX', 'ABC', 'IJK', 'OPQ', 1, 3, 'Four', 'eleven']




```python
list
```




    ['CD',
     'MN',
     'OP',
     'QR',
     'ST',
     'UV',
     'WX',
     'YZ',
     'ABC',
     'EFG',
     'IJK',
     'LMN',
     'OPQ',
     'RST',
     1,
     2,
     3,
     4,
     'Four',
     'twenty',
     'eleven',
     'twelve']




```python
# Remove every 3rd item
del list[::3]
```


```python
list
```




    ['MN',
     'OP',
     'ST',
     'UV',
     'YZ',
     'ABC',
     'IJK',
     'LMN',
     'RST',
     1,
     3,
     4,
     'twenty',
     'eleven']




```python
# Remove every 2nd item
del list[::-3]
```


```python
list
```




    ['MN', 'ST', 'UV', 'ABC', 'IJK', 'RST', 1, 4, 'twenty']




```python
for i, j in enumerate(list):
    print(i, j)
```

    0 MN
    1 ST
    2 UV
    3 ABC
    4 IJK
    5 RST
    6 1
    7 4
    8 twenty
    


```python
item_index = 1, 4
```


```python
list = [value for key, value in enumerate(list) if key not in item_index]
```


```python
list
```




    ['MN', 'UV', 'ABC', 'RST', 1, 4, 'twenty']




```python
lst = [3, 1, 4, 1, 5]
```


```python
print(sorted(lst, reverse=True))
```

    [5, 4, 3, 1, 1]
    


```python
lst2 = lst[:]
```


```python
print(lst2 is lst, lst2 == lst)
```

    False True
    


```python
print(lst[::-1])
```

    [5, 1, 4, 1, 3]
    


```python
lst3 = [[1,2],[3,4]]
```


```python
print([x for row in lst3 for x in row])

```

    [1, 2, 3, 4]
    


```python
print([row[0] for row in lst3])

```

    [1, 3]
    


```python
print(any([]), all([]))
```

    False True
    


```python
print(min([5, 2, 9], key=lambda x: -x))
```

    9
    


```python
print(max([5, 2, 9], key=lambda x: -x))
```

    2
    


```python
print([(i, val) for i, val in enumerate(["a", "b"])])
```

    [(0, 'a'), (1, 'b')]
    


```python
print([None]*5)
```

    [None, None, None, None, None]
    


```python
print([[] for _ in range(3)])
```

    [[], [], []]
    


```python
print([x+y for x,y in zip([1,2], [3,4])])

```

    [4, 6]
    


```python
lst = [1,2,3]
lst *= 2
print(lst)
```

    [1, 2, 3, 1, 2, 3]
    


```python
list = [1, 2, 3]

```


```python
del list

```


```python
print(list(reversed([1,2,3])))  # [3,2,1]

```

    [3, 2, 1]
    


```python
lst = [1,2,3]
```


```python
lst *= 2
```


```python
print(lst)
```

    [1, 2, 3, 1, 2, 3]
    


```python
print(list(map(str.upper, ["a", "b", "c"])))
```

    ['A', 'B', 'C']
    


```python
print(list(filter(str.islower, ["a", "B", "c"])))

```

    ['a', 'c']
    


```python
print([bool(x) for x in [0, 1, "", "text"]])
```

    [False, True, False, True]
    


```python
lst = [5, 4, 3, 2, 1]
```


```python
lst.sort()
```


```python
print(lst)
```

    [1, 2, 3, 4, 5]
    


```python
lst = [1, 2, 3, 4, 5]
```


```python
lst[1:4] = [99, 100]
```


```python
print(lst)
```

    [1, 99, 100, 5]
    


```python
lst = [1, 2, 3]
```


```python
lst[1:2] = []
```


```python
print(lst)
```

    [1, 3]
    


```python
lst = [1, 2, 3]
```


```python
lst[:] = [0]
```


```python
print(lst)
```

    [0]
    


```python
print([x for x in [1,2,3] if x % 2 == 0])
```

    [2]
    


```python
print([i for i in range(3, -1, -1)])

```

    [3, 2, 1, 0]
    


```python
print(list(filter(None, [0, False, 1, 2, None])))
```

    [1, 2]
    


```python
print([i for i in range(3) if i not in [1]])
```

    [0, 2]
    


```python
matrix = [[1, 2], [3, 4]]
```


```python
transposed = list(zip(*matrix))
```


```python
print(transposed)
```

    [(1, 3), (2, 4)]
    


```python
print([list(t) for t in zip(*matrix)])
```

    [[1, 3], [2, 4]]
    


```python
print(all(i < 10 for i in [1, 2, 3]))
```

    True
    


```python
print(any(i > 3 for i in [1, 2, 4]))
```

    True
    


```python
print([i for i in range(10) if i not in [2,5,7]])

```

    [0, 1, 3, 4, 6, 8, 9]
    


```python
print([x for x in [None, 0, "", "Hi"] if x])

```

    ['Hi']
    


```python
print(["even" if i % 2 == 0 else "odd" for i in range(5)])

```

    ['even', 'odd', 'even', 'odd', 'even']
    


```python
print([i*j for i in range(1,4) for j in range(1,4)])
```

    [1, 2, 3, 2, 4, 6, 3, 6, 9]
    


```python
print([round(i/2,1) for i in range(5)])

```

    [0.0, 0.5, 1.0, 1.5, 2.0]
    


```python
print([(x, x**2) for x in range(4)])
```

    [(0, 0), (1, 1), (2, 4), (3, 9)]
    


```python
print([i for i in range(100) if i % 10 == 0])
```

    [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    


```python
print(list(str(i) for i in range(5)))

```

    ['0', '1', '2', '3', '4']
    


```python
lst = [1, 2, 3]
```


```python
a, b, c = lst
```


```python
print(a, b, c)
```

    1 2 3
    


```python
lst = [1, 2, 3]
```


```python
a, *rest = lst
```


```python
print(a, rest)
```

    1 [2, 3]
    


```python
print([i for i in range(10) if i not in (3,6)])
```

    [0, 1, 2, 4, 5, 7, 8, 9]
    


```python
print([[i for i in range(3)] for _ in range(3)])
```

    [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
    


```python
print([sum(row) for row in [[1,2],[3,4]]])
```

    [3, 7]
    


```python
print([row[::-1] for row in [[1,2],[3,4]]])
```

    [[2, 1], [4, 3]]
    


```python
print(["Yes" if x > 0 else "No" for x in [-1, 0, 1]])
```

    ['No', 'No', 'Yes']
    


```python
print(["FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else i for i in range(1,21)])
```

    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz']
    


```python
print(list(zip("abc", [1,2,3])))
```

    [('a', 1), ('b', 2), ('c', 3)]
    


```python
print([*range(5)])
```

    [0, 1, 2, 3, 4]
    


```python
print([chr(i) for i in range(97, 100)])
```

    ['a', 'b', 'c']
    


```python
print([ord(c) for c in "abc"])
```

    [97, 98, 99]
    


```python
print(["{}:{}".format(i,i**2) for i in range(3)])
```

    ['0:0', '1:1', '2:4']
    


```python
print(list(filter(lambda x: x > 2, [1,2,3,4])))
```

    [3, 4]
    


```python
print(list(map(lambda x: x**3, [1,2,3])))
```

    [1, 8, 27]
    


```python
print(list(map(lambda x,y: x+y, [1,2], [3,4])))


```

    [4, 6]
    


```python
print([i for i in range(3) for _ in range(2)])
```

    [0, 0, 1, 1, 2, 2]
    


```python
print([i for _ in range(2) for i in range(3)])
```

    [0, 1, 2, 0, 1, 2]
    


```python
print([x for x in range(5) if x != 2])

```

    [0, 1, 3, 4]
    


```python
print([[i+j for j in range(3)] for i in range(3)])
```

    [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
    


```python
print(["Yes" if i%2==0 else "No" for i in range(4)])
```

    ['Yes', 'No', 'Yes', 'No']
    


```python
print(["*"*i for i in range(5)])
```

    ['', '*', '**', '***', '****']
    


```python
print([" ".join([str(j) for j in range(i)]) for i in range(5)])

```

    ['', '0', '0 1', '0 1 2', '0 1 2 3']
    


```python
print([[i]*i for i in range(5)])
```

    [[], [1], [2, 2], [3, 3, 3], [4, 4, 4, 4]]
    


```python
print(["even"*(i%2==0) or "odd" for i in range(5)])
```

    ['even', 'odd', 'even', 'odd', 'even']
    


```python
print([i for i in range(10) if i & 1 == 0])
```

    [0, 2, 4, 6, 8]
    


```python
print([i for i in range(10) if bin(i)[-1] == "1"])

```

    [1, 3, 5, 7, 9]
    


```python
print(list(set([1,2,2,3])))
```

    [1, 2, 3]
    


```python
print(set([1,2]) & set([2,3]))
```

    {2}
    


```python
print(set([1,2]) | set([3,4]))
```

    {1, 2, 3, 4}
    


```python
print(set([1,2]) - set([2]))
```

    {1}
    


```python

```


---
**Score: 140**