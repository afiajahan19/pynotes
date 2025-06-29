---
title: 1-String
date: 2025-06-29
author: Your Name
cell_count: 119
score: 115
---

```python
a, b = "apple", "banana"
```


```python
print(a + b)
```

    applebanana
    


```python
print(a * 2)
```

    appleapple
    


```python
print(len(a))
```

    5
    


```python
print(a[0])
```

    a
    


```python
print(a[-1])
```

    e
    


```python
print(a[1:4])
```

    ppl
    


```python
print(a[:3])
```

    app
    


```python
print(a[2:])
```

    ple
    


```python
print(a.upper())
```

    APPLE
    


```python
print(a.lower())
```

    apple
    


```python
print(a.capitalize())
```

    Apple
    


```python
print("HELLO".casefold())
```

    hello
    


```python
print(a.swapcase()) 
```

    APPLE
    


```python
print("Hello World".title()) 
```

    Hello World
    


```python
print("   spaced   ".strip())
```

    spaced
    


```python
print("   spaced   ".lstrip())
```

    spaced   
    


```python
print("   spaced   ".rstrip())
```

       spaced
    


```python
print("east-west".split("-"))
```

    ['east', 'west']
    


```python
print("one two three".split())
```

    ['one', 'two', 'three']
    


```python
print("a,b,c".split(","))
```

    ['a', 'b', 'c']
    


```python
print(",".join(["a","b","c"]))
```

    a,b,c
    


```python
print("apple".startswith("app"))
```

    True
    


```python
print("apple".endswith("ple"))
```

    True
    


```python
print("apple".find("p")) 
```

    1
    


```python
print("apple".find("x"))
```

    -1
    


```python
print("apple".index("p")) 
```

    1
    


```python
print("apple".count("p"))
```

    2
    


```python
print("apple".replace("p", "b"))
```

    abble
    


```python
print(" a | b | c ".split("|"))
```

    [' a ', ' b ', ' c ']
    


```python
print("abc".isalpha()) 
```

    True
    


```python
print("abc123".isalnum())
```

    True
    


```python
print("123".isdigit())
```

    True
    


```python
print("   ".isspace())
```

    True
    


```python
print("Hello".islower()) 
```

    False
    


```python
print("hello".islower())
```

    True
    


```python
print("WORLD".isupper())
```

    True
    


```python
print("Hello".istitle())
```

    True
    


```python
print("Hello".encode())
```

    b'Hello'
    


```python
print(str(123)) 
```

    123
    


```python
print(repr("123\n"))
```

    '123\n'
    


```python
print(a.endswith(("le","na")))
```

    True
    


```python
print("abcDEF".upper().lower())
```

    abcdef
    


```python
print("a b c".replace(" ", "")) 
```

    abc
    


```python
print("12345".zfill(8))
```

    00012345
    


```python
print("x".rjust(3, "-"))
```

    --x
    


```python
print("x".ljust(3, "+"))
```

    x++
    


```python
print("hi".center(6, "*"))
```

    **hi**
    


```python
print("aBc".center(5))
```

     aBc 
    


```python
print("ABCD".islower())
```

    False
    


```python
print("abcd".islower())
```

    True
    


```python
print("ABCD".isupper()) 
```

    True
    


```python
print("abc123".islower()) 
```

    True
    


```python
print("abc123".isalpha())
```

    False
    


```python
print("abc".isdigit())
```

    False
    


```python
print("123abc".isalnum())
```

    True
    


```python
print("ß".casefold())
```

    ss
    


```python
print("Straße".casefold())
```

    strasse
    


```python
print("  Hello  ".strip().upper()) 
```

    HELLO
    


```python
print("-".join("ABC")) 
```

    A-B-C
    


```python
print("A-B-C".split("-"))
```

    ['A', 'B', 'C']
    


```python
print("  mixedCase  ".swapcase())
```

      MIXEDcASE  
    


```python
print("python3.9".partition("."))
```

    ('python3', '.', '9')
    


```python
print("nosplit".partition("."))
```

    ('nosplit', '', '')
    


```python
print("a b c".rpartition(" "))
```

    ('a b', ' ', 'c')
    


```python
print("abc\nxyz".splitlines())
```

    ['abc', 'xyz']
    


```python
print("abc\nxyz\n".splitlines(True))
```

    ['abc\n', 'xyz\n']
    


```python
print("for\tj".expandtabs(4))
```

    for j
    


```python
print("teSt".capitalize())
```

    Test
    


```python
print("🙂😊🙃".encode('utf-8'))
```

    b'\xf0\x9f\x99\x82\xf0\x9f\x98\x8a\xf0\x9f\x99\x83'
    


```python
print(" trim ".strip("*"))
```

     trim 
    


```python
print("***trim***".strip("*"))
```

    trim
    


```python
print("abc".startswith(""))
```

    True
    


```python
print("".join([]))
```

    
    


```python
print("".join(["a"]))
```

    a
    


```python
print("One".lower().startswith("o"))
```

    True
    


```python
print("One".upper().endswith("E"))
```

    True
    


```python
print("spam eggs".replace("eggs","ham"))
```

    spam ham
    


```python
print(" x ".strip().zfill(4))
```

    000x
    


```python
print(" x ".strip().zfill(4))
```

    000x
    


```python
print("²³".isnumeric())  
```

    True
    


```python
print("Ⅻ".isnumeric())
```

    True
    


```python
print("20".isdecimal())
```

    True
    


```python
print("²".isdecimal())
```

    False
    


```python
print("hello".encode('ascii'))
```

    b'hello'
    


```python
print("a b c".replace(" ", "-", 2))
```

    a-b-c
    


```python
print("a--b--c".split("--",1)) 
```

    ['a', 'b--c']
    


```python
print("A|B|C".split("|", maxsplit=1))
```

    ['A', 'B|C']
    


```python
print("  A  B  ".split())
```

    ['A', 'B']
    


```python
print("word".ljust(6)) 
```

    word  
    


```python
print("word".rjust(6)) 
```

      word
    


```python
print("WORD".lower().upper())
```

    WORD
    


```python
print(" a,b,c ".strip().split(","))
```

    ['a', 'b', 'c']
    


```python
print(";".join("123"))
```

    1;2;3
    


```python
print("123".join(["a","b","c"])) 
```

    a123b123c
    


```python
print("x".center(3))
```

     x 
    


```python
print("x".center(4,"-"))
```

    -x--
    


```python
print("Data".islower(), "Data".isupper(), "Data".istitle())
```

    False False True
    


```python
print("Data123".isalnum())
```

    True
    


```python
print("  ".replace(" ","_"))
```

    __
    


```python
print("A\nB\nC".splitlines())
```

    ['A', 'B', 'C']
    


```python
print("\n".join(["A","B","C"]))
```

    A
    B
    C
    


```python
print("trimmeR".rstrip("Rr"))
```

    trimme
    


```python
print("trimmeR".lstrip("tr"))
```

    immeR
    


```python
print("foobar".partition("o"))
```

    ('f', 'o', 'obar')
    


```python
print("foobar".rpartition("o"))
```

    ('fo', 'o', 'bar')
    


```python
print(" repeat ".strip().replace(" ","-"))
```

    repeat
    


```python
print(" repeat ".strip().replace(" ", "-"))
```

    repeat
    


```python
print("aBcDeF".swapcase()[::-1]) 
```

    fEdCbA
    


```python
print("12345".translate(str.maketrans("135","ACE")))
```

    A2C4E
    


```python
print("hello😊".encode('utf-8').decode('utf-8'))
```

    hello😊
    


```python
print("test".format())
```

    test
    


```python
print("{0} + {1}".format("a","b"))
```

    a + b
    


```python
print(f"{a}-{b}") 
```

    apple-banana
    


```python
print("%s:%d" % ("age", 30)) 
```

    age:30
    


```python
print(" abc ".strip().title())
```

    Abc
    


```python
print("mix".zfill(5).upper())
```

    00MIX
    


```python
print("END".center(7, "."))
```

    ..END..
    


```python
print("wrap".rjust(6,"~").ljust(8,"_"))
```


---
**Score: 115**