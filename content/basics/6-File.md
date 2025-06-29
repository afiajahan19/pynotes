---
title: 6-File
date: 2025-06-29
author: Your Name
cell_count: 106
score: 105
---

```python
#Basic File Reading/Writing
```


```python
f = open("sample.txt", "w")
f.write("Hello")
f.close()
```


```python
f = open("sample.txt", "r")
print(f.read())
f.close()
```

    Hello
    


```python
with open("sample.txt", "r") as f:
    print(f.read())
```

    Hello
    


```python
with open("sample.txt", "w") as f:
    f.write("New content")

```


```python
with open("sample.txt", "a") as f:
    f.write("\nAppended line")
```


```python
with open("sample.txt", "r") as f:
    print(f.readline())
```

    New content
    
    


```python
with open("sample.txt", "r") as f:
    print(f.readlines())
```

    ['New content\n', 'Appended line']
    


```python
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())
```

    New content
    Appended line
    


```python
with open("sample.txt", "r") as f:
    data = f.read(5)
    print(data)

```

    New c
    


```python
with open("sample.txt", "r") as f:
    f.seek(0)
    print(f.read(4))
```

    New 
    


```python
with open("sample.txt", "r") as f:
    print(f.tell())  # cursor position
```

    0
    


```python
with open("sample.txt", "r") as f:
    f.seek(2)
    print(f.read(3))
    
```

    w c
    


```python
with open("sample.txt", "r") as f:
    for i, line in enumerate(f):
        print(f"{i}: {line.strip()}")
```

    0: New content
    1: Appended line
    


```python
try:
    with open("not_exist.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")

```

    File not found
    


```python
with open("sample.txt", "w+") as f:
    f.write("Test")
    f.seek(0)
    print(f.read())
```

    Test
    


```python
with open("sample.txt", "a+") as f:
    f.write("\nAgain")
    f.seek(0)
    print(f.read())
```

    Test
    Again
    


```python
with open("sample.txt", "r") as f:
    chars = list(f.read())
    print(chars)

```

    ['T', 'e', 's', 't', '\n', 'A', 'g', 'a', 'i', 'n']
    


```python
with open("sample.txt", "r") as f:
    words = f.read().split()
    print(words)

```

    ['Test', 'Again']
    


```python
lines = ["Line1\n", "Line2\n", "Line3\n"]
with open("sample.txt", "w") as f:
    f.writelines(lines)
```


```python
with open("sample.txt", "r") as f:
    print(f.read().upper())
```

    LINE1
    LINE2
    LINE3
    
    


```python
with open("sample.txt", "r") as f:
    print(f.read().lower())

```

    line1
    line2
    line3
    
    


```python
with open("sample.txt", "r") as f:
    print(f.read().splitlines())

```

    ['Line1', 'Line2', 'Line3']
    


```python
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(lines[::-1])  # reversed
```

    ['Line3\n', 'Line2\n', 'Line1\n']
    


```python
with open("sample.txt", "r") as f:
    print(sum(1 for _ in f))  # line count
```

    3
    


```python
with open("sample.txt", "r") as f:
    print(len(f.read().split()))  # word count

```

    3
    


```python
with open("sample.txt", "r") as f:
    print(len(f.read()))  # char count


```

    18
    


```python
with open("sample.txt", "r") as f:
    longest = max(f, key=len)
    print(longest.strip())
```

    Line1
    


```python
with open("sample.txt", "r") as f:
    for line in f:
        if "Line" in line:
            print(line.strip())
```

    Line1
    Line2
    Line3
    


```python
with open("sample.txt", "r") as f:
    print(any("Line2" in line for line in f))
```

    True
    


```python
with open("sample.txt", "r") as f:
    print(all("Line" in line for line in f))

```

    True
    


```python
#File Paths, Encodings, Errors
```


```python
with open("sample.txt", encoding="utf-8") as f:
    print(f.read())
```

    Line1
    Line2
    Line3
    
    


```python
try:
    with open("sample.txt", "x") as f:
        f.write("new file")
except FileExistsError:
    print("Already exists")
```

    Already exists
    


```python
import os
print(os.path.exists("sample.txt"))
```

    True
    


```python
os.remove("sample.txt")
```


```python
with open("newfile.txt", "w") as f:
    f.write("temporary")
os.rename("newfile.txt", "renamed.txt")
```


```python
os.mkdir("test_dir")

```


```python
os.rmdir("test_dir")

```


```python
print(os.getcwd())
```

    C:\tact\pynotes\notebooks\basics
    


```python
os.chdir("..")
```


```python
print(os.getcwd())
```

    C:\tact\pynotes\notebooks
    


```python
from pathlib import Path
print(Path("sample.txt").exists())

```

    False
    


```python
Path("sample.txt").write_text("Written by pathlib")

```




    18




```python
Path("sample.txt").unlink()  # delete
```


```python
Path("folder").mkdir(exist_ok=True)
```


```python
Path("folder/sample.txt").write_text("In folder")
```




    9




```python
p = Path("folder/sample.txt")
```


```python
print(p.name, p.suffix, p.stem)

```

    sample.txt .txt sample
    


```python
print(p.parent)
```

    folder
    


```python
print(list(Path(".").glob("*.txt")))

```

    []
    


```python
print(p.resolve())

```

    C:\tact\pynotes\notebooks\folder\sample.txt
    


```python
with open("binary.bin", "wb") as f:
    f.write(b"binary data")
```


```python
with open("binary.bin", "rb") as f:
    print(f.read())
```

    b'binary data'
    


```python
with open("sample.txt", "w", errors="ignore") as f:
    f.write("ignored")
```


```python
Path("utf.txt").write_text("नमस्ते", encoding="utf-8")
```




    6




```python
print(Path("utf.txt").read_text(encoding="utf-8"))
```

    नमस्ते
    


```python
print("utf.txt" in os.listdir())
```

    True
    


```python
print(os.listdir("."))

```

    ['basics', 'binary.bin', 'folder', 'pandas-work', 'sample.txt', 'utf.txt']
    


```python
print([f for f in os.listdir() if f.endswith(".txt")])

```

    ['sample.txt', 'utf.txt']
    


```python
Path("file_with_space.txt").write_text("spacing")

```




    7




```python
with open("file_with_space.txt", "r") as f:
    print(f.read().replace(" ", "_"))

```

    spacing
    


```python
with open("sample.txt", "a") as f:
    f.write("\nLast line")
```


```python
#CSV, JSON, Pickle
```


```python
import csv
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 30])

```


```python
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

    ['Name', 'Age']
    ['Alice', '30']
    


```python
import json
data = {"name": "Alice", "age": 30}
with open("data.json", "w") as f:
    json.dump(data, f)
```


```python
with open("data.json", "r") as f:
    print(json.load(f))

```

    {'name': 'Alice', 'age': 30}
    


```python
print(json.dumps(data)) 
```

    {"name": "Alice", "age": 30}
    


```python
print(json.loads('{"key": 1}'))
```

    {'key': 1}
    


```python
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

```


```python
import pickle
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)
```


```python
with open("data.pkl", "rb") as f:
    print(pickle.load(f))
```

    {'name': 'Alice', 'age': 30}
    


```python
try:
    with open("non_existing.txt", "r") as f:
        pass
except FileNotFoundError as e:
    print(e)
```

    [Errno 2] No such file or directory: 'non_existing.txt'
    


```python
#Advanced/Tricks/Useful Patterns
```


```python
with open("numbers.txt", "w") as f:
    f.write("\n".join(str(i) for i in range(10)))
```


```python
with open("numbers.txt", "r") as f:
    print([int(line) for line in f])
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    


```python
with open("file.txt", "w") as f:
    pass  # creates empty file
```


```python
print(os.stat("file.txt").st_size)  # file size
```

    0
    


```python
with open("log.txt", "a") as f:
    f.write("Log entry\n")
```


```python
with open("multi.txt", "w") as f:
    f.write("Line1\nLine2\nLine3\n")

```


```python
with open("multi.txt") as f:
    print(f.readlines()[1])  # second line

```

    Line2
    
    


```python
lines = Path("multi.txt").read_text().splitlines()
print(lines[-1])  # last line
```

    Line3
    


```python
lines[1] = "Updated line2"
Path("multi.txt").write_text("\n".join(lines))
```




    25




```python
with open("read.txt", "w") as f:
    f.write("123abc456")
```


```python
with open("read.txt", "r") as f:
    print("abc" in f.read())
```

    True
    


```python
f = open("late.txt", "w")
f.write("oops")
f.close()
```


```python
with open("late.txt", "r+") as f:
    f.seek(0)
    f.write("fixed")

```


```python
with open("space.txt", "w") as f:
    f.write("   line with space   ")
```


```python
with open("space.txt") as f:
    print(f.read().strip())
```

    line with space
    


```python
with open("csv2.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "score"])
    writer.writeheader()
    writer.writerow({"id": 1, "score": 90})
```


```python
with open("csv2.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["score"])

```

    90
    


```python
with open("utf8.txt", "w", encoding="utf-8") as f:
    f.write("¡Hola!")
```


```python
with open("utf8.txt", encoding="utf-8") as f:
    print(f.read())

```

    ¡Hola!
    


```python
Path("delete_me.txt").write_text("bye")
Path("delete_me.txt").unlink()
```


```python
try:
    Path("badfile.txt").read_text()
except FileNotFoundError:
    print("No such file")
```

    No such file
    


```python
with open("even.txt", "w") as f:
    f.writelines([f"{i}\n" for i in range(0, 10, 2)])

```


```python
with open("even.txt") as f:
    evens = [int(line) for line in f]
    print(evens)
```

    [0, 2, 4, 6, 8]
    


```python
print(os.path.abspath("sample.txt"))
```

    C:\tact\pynotes\notebooks\sample.txt
    


```python
print(os.path.basename("folder/sample.txt"))

```

    sample.txt
    


```python
print(os.path.dirname("folder/sample.txt"))
```

    folder
    


```python
print(os.path.splitext("file.txt"))  # ('file', '.txt')

```

    ('file', '.txt')
    


```python
print(Path("folder/file.txt").with_suffix(".bak"))

```

    folder\file.bak
    


```python
with open("caps.txt", "w") as f:
    f.write("hello\nworld")

```


```python
with open("caps.txt") as f:
    print([line.upper() for line in f])
```

    ['HELLO\n', 'WORLD']
    


```python

```


---
**Score: 105**