---
title: Random-Module
date: 2025-06-29
author: Your Name
cell_count: 157
score: 155
---

```python
import random
```


```python
print(random.random())
```

    0.487560015622336
    


```python
print(random.randint(1, 10))

```

    6
    


```python
print(random.randrange(0, 20, 2))

```

    12
    


```python
print(random.choice(['red', 'green', 'blue']))
```

    red
    


```python
print(random.choices(['A', 'B', 'C'], k=5))
```

    ['C', 'B', 'C', 'B', 'A']
    


```python
print(random.choices(['A', 'B', 'C'], k=5))
```

    ['A', 'C', 'C', 'C', 'B']
    


```python
print(random.uniform(10, 20))
```

    17.44199624104448
    


```python
print(random.getrandbits(4))
```

    10
    


```python
print(random.choice((10, 20, 30)))
```

    20
    


```python
print(random.choice("Python"))
```

    y
    


```python
s = list("hello")
random.shuffle(s)
print("".join(s))
```

    helol
    


```python
colors = ['red', 'blue', 'green']
print(colors[random.randrange(len(colors))])
```

    red
    


```python
print(random.sample(range(1, 20), 5))
```

    [3, 16, 6, 11, 13]
    


```python
print(random.randint(1, 6))
```

    5
    


```python
print("Heads" if random.randint(0, 1) == 0 else "Tails")
```

    Heads
    


```python
print(round(random.uniform(0, 100), 2))
```

    23.06
    


```python
print(random.choice([True, False]))
```

    True
    


```python
print(random.choices(range(10), k=3))
```

    [2, 4, 6]
    


```python
print(random.choices(['low', 'mid', 'high'], weights=[1, 3, 6], k=1))
```

    ['mid']
    


```python
print(random.choices(['x', 'y', 'z'], k=3))
```

    ['y', 'x', 'z']
    


```python
#Seeding
```


```python
random.seed(10)
print(random.random())
```

    0.5714025946899135
    


```python
random.seed(123)
print(random.randint(1, 100))
```

    7
    


```python
random.seed(50)
a = random.random()
random.seed(50)
b = random.random()
print(a == b)  # True
```

    True
    


```python
import time
random.seed(time.time())

```


```python
random.seed("hello")
print(random.random())
```

    0.3537754404730722
    


```python
def get_random_with_seed(seed_val):
    random.seed(seed_val)
    return random.randint(1, 100)

print(get_random_with_seed(42))
```

    82
    


```python
lst = [1, 2, 3, 4, 5]
random.seed(2)
random.shuffle(lst)
print(lst)
```

    [3, 2, 4, 5, 1]
    


```python
random.seed(4)
print(random.sample(range(1, 100), 5))

```

    [31, 39, 14, 93, 51]
    


```python
random.seed(999)
print(random.random())
```

    0.7813468849570298
    


```python
for i in range(5):
    random.seed(i)
    print(random.randint(1, 10))
```

    7
    3
    1
    4
    4
    


```python
#Statistical Distributions
```


```python
print(random.uniform(1, 10))
```

    3.7296872729695907
    


```python
print(random.gauss(0, 1))
```

    -0.20535732231241616
    


```python
print(random.normalvariate(0, 1))
```

    0.11926168260455533
    


```python
print(random.triangular(1, 100, 50))

```

    92.97311499109534
    


```python
print(random.betavariate(2, 5))
```

    0.08904379481080787
    


```python
print(random.expovariate(1.5))
```

    1.1691481464621643
    


```python
print(random.gammavariate(2, 3))
```

    3.297017627578116
    


```python
print(random.lognormvariate(0, 0.5))
```

    0.753985601257307
    


```python
print(random.vonmisesvariate(0, 1))

```

    0.25594792444230136
    


```python
print(random.paretovariate(2.5))
```

    3.6578959596970564
    


```python
print(random.weibullvariate(1, 1.5))
```

    1.5272270713856133
    


```python
scores = [random.normalvariate(70, 10) for _ in range(5)]
print(scores)
```

    [55.89574778343234, 65.44265505925276, 64.27624374716605, 57.90449889121083, 56.24625556120736]
    


```python
from collections import Counter
values = [round(random.gauss(50, 15)) for _ in range(1000)]
hist = Counter(values)
print(hist.most_common(5))
```

    [(58, 36), (46, 32), (43, 30), (47, 28), (53, 28)]
    


```python
values = [random.gauss(50, 5) for _ in range(1000)]
print(min(values), max(values))

```

    29.66666037117583 67.03237989352832
    


```python
import statistics
data = [random.gauss(100, 20) for _ in range(1000)]
print(statistics.mean(data), statistics.stdev(data))
```

    100.99849912914817 21.406751963222828
    


```python
print(random.triangular(0, 10, 8))
```

    4.979361550949488
    


```python
print(random.normalvariate(170, 10))
```

    162.17402561610336
    


```python
print(random.lognormvariate(0.02, 0.05))
```

    0.9653176706571646
    


```python
print(random.weibullvariate(1, 1.5))
```

    1.043084668057772
    


```python
print([round(random.gammavariate(2, 1), 2) for _ in range(5)])

```

    [0.93, 2.61, 2.97, 1.65, 3.69]
    


```python
print(random.choice(["rock", "paper", "scissors"]))
```

    paper
    


```python
for _ in range(10):
    print("Heads" if random.randint(0, 1) == 0 else "Tails")
```

    Tails
    Tails
    Heads
    Heads
    Heads
    Tails
    Heads
    Tails
    Heads
    Heads
    


```python
print([random.randint(1, 6) for _ in range(5)])
```

    [5, 5, 3, 4, 3]
    


```python
print(random.randint(0, 36))
```

    30
    


```python
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [f"{r} of {s}" for r in ranks for s in suits]
print(random.choice(deck))

```

    7 of Hearts
    


```python
random.shuffle(deck)
print(deck[:5])

```

    ['3 of Hearts', '6 of Hearts', '8 of Spades', '5 of Clubs', '5 of Diamonds']
    


```python
print(sum([random.randint(1, 6) for _ in range(2)]))

```

    8
    


```python
d1, d2 = random.randint(1, 6), random.randint(1, 6)
print("Snake eyes!" if d1 == d2 == 1 else f"{d1}, {d2}")
```

    4, 5
    


```python
print(random.sample(range(1, 50), 6))
```

    [6, 12, 2, 35, 28, 18]
    


```python
makes = sum(random.choices([1, 0], weights=[0.8, 0.2], k=10))
print(f"Makes: {makes}")
```

    Makes: 6
    


```python
print([random.choice(['H', 'T']) for _ in range(100)].count('H'))
```

    46
    


```python
print(random.uniform(0, 360))
```

    327.2638114387294
    


```python
print((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
```

    (166, 13, 129)
    


```python
def play_rps():
    return random.choice(['rock', 'paper', 'scissors'])
print(play_rps())
```

    paper
    


```python
print(random.randint(1990, 2025))
```

    1991
    


```python
print(random.random() < 0.5)
```

    True
    


```python
print(random.choice(['up', 'down', 'left', 'right']))
```

    right
    


```python
print(random.randint(1, 8))
```

    3
    


```python
print(sorted([random.randint(1, 6) for _ in range(3)]))
```

    [1, 3, 4]
    


```python
print(random.choices([1,2,3,4,5,6], weights=[1,1,1,1,1,5], k=1))
```

    [6]
    


```python
import string

# 71. Random digit
print(random.choice(string.digits))
```

    6
    


```python
print(random.choice(string.ascii_lowercase))
```

    g
    


```python
print(random.choice(string.ascii_uppercase))
```

    I
    


```python
print(random.choice(string.ascii_uppercase))
```

    K
    


```python
print(''.join(random.choices(string.digits, k=6)))
```

    946030
    


```python
chars = string.ascii_letters + string.digits
print(''.join(random.choices(chars, k=8)))
```

    P4PPbPxx
    


```python
chars = string.ascii_letters + string.digits + string.punctuation
print(''.join(random.choices(chars, k=10)))

```

    %u?q"6SMhU
    


```python
passwords = [''.join(random.choices(chars, k=8)) for _ in range(5)]
print(passwords)

```

    ['KqbL3F>0', "'8M(CuE!", 'lm)Sy>@m', 'Q,.jFUd[', 'yGAE"-Xv']
    


```python
pwd = random.choice(string.ascii_uppercase) + \
      random.choice(string.digits) + \
      random.choice(string.punctuation) + \
      ''.join(random.choices(string.ascii_lowercase, k=5))
print(''.join(random.sample(pwd, len(pwd))))
```

    `3afWfhy
    


```python
print(''.join(random.choices(string.ascii_letters + string.digits, k=32)))
```

    pFAS20nvJS9P5H9L9Wzkk8jkIpgGP89y
    


```python
mac = ":".join(f"{random.randint(0, 255):02x}" for _ in range(6))
print(mac)
```

    d4:07:fa:5f:8e:cf
    


```python
print('#' + ''.join(random.choices('0123456789ABCDEF', k=6)))
```

    #4F5359
    


```python
print(''.join(random.choices(string.ascii_uppercase, k=2)) + '-' + ''.join(random.choices(string.digits, k=4)))
```

    JA-1239
    


```python
print('user' + str(random.randint(1000, 9999)))
```

    user4541
    


```python
print('file_' + str(random.randint(10000, 99999)) + '.txt')
```

    file_96398.txt
    


```python
print(random.choice(['.txt', '.csv', '.json', '.xml']))
```

    .json
    


```python
print(''.join(random.choices('0123456789abcdef', k=4)))

```

    7188
    


```python
print('user_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)))
```

    user_4d1wmt
    


```python
print(''.join(random.choices(string.digits, k=4)))
```

    7898
    


```python
print(''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k=12)))
```

    YyyP<ze'>r>A
    


```python
#Custom Random Logic & Utilities 
```


```python
print('Heads' if random.random() < 0.7 else 'Tails')
```

    Heads
    


```python
print(random.choice(['Mon', 'Tue', 'Wed', 'Thu', 'Fri']))
```

    Fri
    


```python
def random_bool(p=0.5): return random.random() < p
print(random_bool())
```

    True
    


```python
def random_hex_color(): return '#{:02X}{:02X}{:02X}'.format(*[random.randint(0, 255) for _ in range(3)])
print(random_hex_color())
```

    #669C11
    


```python
print((random.uniform(-10, 10), random.uniform(-10, 10)))
```

    (6.730485397285662, 1.5518531002953715)
    


```python
import math
theta = random.uniform(0, 2 * math.pi)
print((math.cos(theta), math.sin(theta)))
```

    (-0.6462767356050989, 0.7631031260685656)
    


```python
s = "abcdef"
print(''.join(random.sample(s, len(s))))
```

    beadfc
    


```python
print(random.choices(['Yes', 'No'], weights=[0.2, 0.8])[0])
```

    No
    


```python
print(random.choice(list(d.keys())))
```

    a
    


```python
print(random.choice(list(d.values())))
```

    2
    


```python
print(random.choice(list({1, 2, 3, 4, 5})))
```

    1
    


```python
print(random.sample(['a', 'b', 'c', 'd', 'e'], 3))

```

    ['b', 'c', 'a']
    


```python
matrix = [[random.randint(0, 9) for _ in range(3)] for _ in range(3)]
print(matrix)

```

    [[1, 5, 2], [6, 2, 1], [5, 7, 5]]
    


```python
print([[random.random() for _ in range(2)] for _ in range(2)])
```

    [[0.32336223690360333, 0.7452373502161956], [0.14864018081208896, 0.7484333575783582]]
    


```python
print([random.uniform(0, 1) for _ in range(5)])
```

    [0.5246443223938702, 0.4798894073886164, 0.6134321478562901, 0.6963209505143704, 0.8455446857221685]
    


```python
print(random.sample(range(5), 5))

```

    [0, 2, 4, 1, 3]
    


```python
print(random.choice(list(d.items())))
```

    ('a', 1)
    


```python
import time; delay = random.uniform(1, 3); print(f"Sleeping {delay:.2f}s"); time.sleep(delay)
```

    Sleeping 2.35s
    


```python
position = 0
for _ in range(10):
    position += random.choice([-1, 1])
print(position)
```

    2
    


```python
x = y = 0
for _ in range(10):
    dx, dy = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
    x += dx; y += dy
print(x, y)

```

    0 0
    


```python
inside = 0
for _ in range(10000):
    x, y = random.random(), random.random()
    if x**2 + y**2 < 1: inside += 1
print(4 * inside / 10000)
```

    3.1192
    


```python
big_list = list(range(1000))
random.shuffle(big_list)
print(big_list[:10])

```

    [107, 724, 665, 158, 136, 116, 612, 664, 569, 330]
    


```python
print([random.choice(['Yes', 'No']) for _ in range(20)])
```

    ['Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes']
    


```python
print(random.sample("abcdefg", 3))

```

    ['e', 'c', 'a']
    


```python
nested = {'a': {'x': 1}, 'b': {'y': 2}}
print(random.choice(list(nested.values())))
```

    {'y': 2}
    


```python
print(f"{random.randint(0,23):02}:{random.randint(0,59):02}")
```

    08:25
    


```python
print(f"log_{random.randint(100,999)}_{int(time.time())}.txt")
```

    log_851_1751208941.txt
    


```python
lines = ["first", "second", "third"]
print(random.choice(lines))
```

    first
    


```python
def get_random_index(data): return random.randrange(len(data))
print(get_random_index(["apple", "banana", "cherry"]))
```

    2
    


```python
print([random.choice([True, False]) for _ in range(10)])
```

    [True, False, False, True, False, True, False, False, True, False]
    


```python
print(random.random() < 0.3)
```

    False
    


```python
print(random.choices(string.ascii_lowercase, k=5))
```

    ['x', 'q', 'h', 'l', 'c']
    


```python
print(random.choices(string.digits, k=4))
```

    ['1', '4', '6', '4']
    


```python
print(time.time() + random.randint(1000, 10000))
```

    1751216346.3365538
    


```python
target = 50
print(target + random.uniform(-5, 5))
```

    50.356717471190464
    


```python
print(f'{random.uniform(0, 100):.2f}%')
```

    69.27%
    


```python
delay = random.uniform(1, 5)
print(f'Delay: {delay:.1f}s')
```

    Delay: 2.5s
    


```python
print(random.choice(['Keep going!', 'Try again.', 'Well done!']))
```

    Well done!
    


```python
print(random.choice([x for x in range(3, 100, 3)]))
```

    84
    


```python
#General Random Values
```


```python
for _ in range(30):
    print(random.randint(1, 100), random.uniform(0, 1))
```

    84 0.3767823050705269
    34 0.4996558877437687
    79 0.691240369351869
    99 0.26840410858727115
    7 0.7098460181243668
    5 0.8754797296152051
    9 0.09412814389266544
    78 0.9096059220019942
    5 0.8753188411501845
    77 0.5846329189786156
    28 0.30413800514907685
    43 0.33514783037780593
    97 0.009804734092744627
    85 0.39609040485009817
    43 0.34107999905789
    29 0.16559751163388514
    78 0.43778708133113475
    12 0.7431437237246094
    84 0.9447745286454454
    95 0.15925379390082173
    93 0.4953117694259682
    95 0.43577383206430387
    72 0.9096394203849415
    26 0.22632158475619757
    71 0.8691104439723106
    97 0.3810684423581878
    68 0.2778499542183084
    84 0.49898121680846474
    95 0.3955579548284107
    72 0.442355738396508
    


```python
#Random Sampling & Generation
```


```python
print(random.choice(range(0, 100, 2)))
```

    52
    


```python
print(random.choice(range(1, 100, 2)))

```

    45
    


```python
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(random.choice(primes))

```

    29
    


```python
print(random.choice('aeiou'))
```

    o
    


```python
print(random.choice([c for c in string.ascii_lowercase if c not in 'aeiou']))
```

    m
    


```python
words = ['life', 'is', 'beautiful', 'random', 'cool', 'great']
print(' '.join(random.choices(words, k=3)))
```

    cool beautiful life
    


```python
print(random.choice(string.printable))
```

    l
    


```python
print(random.choice(range(0, 101, 10)))
```

    0
    


```python
print(random.randint(100000, 999999))
```

    490960
    


```python
print(''.join(random.choices('0123456789abcdef', k=8)))

```

    c8a45e7c
    


```python
print(''.join(random.choices(string.ascii_uppercase, k=2)))
```

    ZJ
    


```python
print('-'.join(random.choices(words, k=3)))

```

    great-cool-beautiful
    


```python
print(f"${random.uniform(1, 500):.2f}")
```

    $181.62
    


```python
print(tuple(random.randint(1, 10) for _ in range(3)))

```

    (1, 3, 4)
    


```python
print(random.choices(['Pass', 'Fail'], weights=[90, 10], k=1)[0])

```

    Pass
    


```python
print('ID-' + ''.join(random.choices(string.ascii_uppercase, k=5)))
```

    ID-MVUSH
    


```python
print(f"{random.randint(1,12)}:{random.randint(0,59):02} {'AM' if random.random()<0.5 else 'PM'}")
```

    11:08 PM
    


```python
print(''.join(random.choices('01', k=8)))
```

    01010000
    


```python
print(''.join(random.choices('012', k=6)))
```

    022102
    


```python
print([[random.randint(0,9) for _ in range(2)] for _ in range(2)])
```

    [[7, 0], [0, 7]]
    


```python

```


---
**Score: 155**