---
title: Math-Module
date: 2025-06-29
author: Your Name
cell_count: 185
score: 185
---

```python
#Number Basics
```


```python
import math
```


```python
print(math.ceil(4.3))
```

    5
    


```python
print(math.floor(4.8))
```

    4
    


```python
print(math.floor(-4.2))
```

    -5
    


```python
print(math.fabs(-3.7))
```

    3.7
    


```python
print(math.fabs(3.7))
```

    3.7
    


```python
print(math.trunc(3.9)) 
```

    3
    


```python
print(math.trunc(-3.9))
```

    -3
    


```python
print(math.copysign(10, -1))
```

    -10.0
    


```python
print(math.copysign(0, -5))
```

    -0.0
    


```python
print(math.fmod(20, 3))
```

    2.0
    


```python
print(math.fmod(7.5, 2.0)) 
```

    1.5
    


```python
print(math.isclose(0.1 + 0.2, 0.3)) 
```

    True
    


```python
print(math.isclose(0.1 + 0.2, 0.3001))  # False

```

    False
    


```python
print(math.remainder(7, 3)) 
```

    1.0
    


```python
print(math.remainder(-7, 3))  # -1.0


```

    -1.0
    


```python
print(math.modf(2.75))  # (0.75, 2.0)
```

    (0.75, 2.0)
    


```python
print(math.isfinite(10))  # True
```

    True
    


```python
print(math.isfinite(math.inf))
```

    False
    


```python
print(math.isnan(math.nan))
```

    True
    


```python
print(math.isnan(5.0)) 
```

    False
    


```python
print(math.isinf(math.inf)) 
```

    True
    


```python
print(math.isinf(100))
```

    False
    


```python
print(math.frexp(8)) 
```

    (0.5, 4)
    


```python
print(math.frexp(10.5)) 
```

    (0.65625, 4)
    


```python
print(math.ldexp(0.5, 3)) 

```

    4.0
    


```python
print(math.ldexp(0.65625, 4))
```

    10.5
    


```python
print(math.copysign(0.0, -0.0)) 
```

    -0.0
    


```python
print(math.modf(0))
```

    (0.0, 0.0)
    


```python
#Power, Roots, and Logarithms 
```


```python
print(math.pow(2, 3))  
```

    8.0
    


```python
print(math.pow(4.5, 2))
```

    20.25
    


```python
print(math.sqrt(16)) 
```

    4.0
    


```python
print(math.sqrt(2.25))
```

    1.5
    


```python
print(math.isqrt(10))
```

    3
    


```python
print(math.isqrt(25))
```

    5
    


```python
print(math.exp(1))
```

    2.718281828459045
    


```python
print(math.exp(-1)) 
```

    0.36787944117144233
    


```python
print(math.expm1(0.01))
```

    0.010050167084168058
    


```python
print(math.log(10))
```

    2.302585092994046
    


```python
print(math.log10(1000)) 
```

    3.0
    


```python
print(math.log2(32))
```

    5.0
    


```python
print(math.log1p(1e-5)) 
```

    9.99995000033333e-06
    


```python
print(math.log(25, 5))
```

    2.0
    


```python
print(math.pow(9, 0.5)) 
```

    3.0
    


```python
print(math.sqrt(0))
```

    0.0
    


```python
print(math.isqrt(0))
```

    0
    


```python
print(math.log1p(0))
```

    0.0
    


```python
print(math.exp(0))
```

    1.0
    


```python
print(math.expm1(0))
```

    0.0
    


```python
print(math.log(1))
```

    0.0
    


```python
print(math.log2(1))
```

    0.0
    


```python
print(math.log10(1))
```

    0.0
    


```python
print(math.pow(2, -2)) 
```

    0.25
    


```python
print(math.log(math.e)) 
```

    1.0
    


```python
print(round(math.exp(5), 2)) 
```

    148.41
    


```python
print(math.pow(10, 6)) 
```

    1000000.0
    


```python
print(math.sqrt(1000000)) 
```

    1000.0
    


```python
try:
    print(math.log(-1))  # Error
except ValueError:
    print("Math domain error")
```

    Math domain error
    


```python
try:
    print(math.sqrt(-9))  # Error
except ValueError:
    print("Math domain error")
```

    Math domain error
    


```python
#Trigonometry Functions 
```


```python
print(math.sin(0))
```

    0.0
    


```python
print(math.sin(math.pi / 2))
```

    1.0
    


```python
print(math.sin(math.pi)) 
```

    1.2246467991473532e-16
    


```python
print(math.cos(0))
```

    1.0
    


```python
print(math.cos(math.pi))
```

    -1.0
    


```python
print(math.tan(0))
```

    0.0
    


```python
print(math.tan(math.pi / 4))
```

    0.9999999999999999
    


```python
try:
    print(math.tan(math.pi / 2))  # very large
except:
    print("Undefined")
```

    1.633123935319537e+16
    


```python
print(math.asin(1)) 

```

    1.5707963267948966
    


```python
print(math.asin(0))
```

    0.0
    


```python
print(math.acos(1))
```

    0.0
    


```python
print(math.acos(0))  
```

    1.5707963267948966
    


```python
print(math.atan(1))
```

    0.7853981633974483
    


```python
print(math.atan(0))
```

    0.0
    


```python
print(math.atan2(1, 1)) 
```

    0.7853981633974483
    


```python
print(math.atan2(-1, -1)) 
```

    -2.356194490192345
    


```python
print(math.sin(-math.pi / 2)) 
```

    -1.0
    


```python
print(math.cos(-math.pi))
```

    -1.0
    


```python
print(math.tan(-math.pi / 4))
```

    -0.9999999999999999
    


```python
try:
    print(math.asin(2))
except ValueError:
    print("Invalid domain")
```

    Invalid domain
    


```python
try:
    print(math.acos(-2))
except ValueError:
    print("Invalid domain")
    
```

    Invalid domain
    


```python
print(math.atan(-1))
```

    -0.7853981633974483
    


```python
print(math.sin(math.radians(30)))
```

    0.49999999999999994
    


```python
print(math.cos(math.radians(60))) 
```

    0.5000000000000001
    


```python
print(math.tan(math.radians(45)))
```

    0.9999999999999999
    


```python
x = math.pi / 6
print(math.asin(math.sin(x))) 
```

    0.5235987755982988
    


```python
print(math.acos(math.cos(x))) 
```

    0.5235987755982987
    


```python
print(math.atan(math.tan(x)))
```

    0.5235987755982988
    


```python
print(math.atan2(0, 0))  
```

    0.0
    


```python
print(math.atan2(1, -1))
```

    2.356194490192345
    


```python
#Angle Conversions & Constants 
```


```python
print(math.degrees(math.pi))  
```

    180.0
    


```python
print(math.degrees(math.pi / 2)) 
```

    90.0
    


```python
print(math.degrees(2 * math.pi))
```

    360.0
    


```python
print(math.radians(180))
```

    3.141592653589793
    


```python
print(math.radians(90)) 
```

    1.5707963267948966
    


```python
print(math.radians(360))
```

    6.283185307179586
    


```python
print(math.hypot(3, 4)) 
```

    5.0
    


```python
print(math.hypot(0, 5))
```

    5.0
    


```python
print(math.hypot(-3, 4))
```

    5.0
    


```python
print(math.isclose(1.0001, 1.0002, rel_tol=1e-3)) 
```

    True
    


```python
print(math.pi)  
```

    3.141592653589793
    


```python
print(math.e)
```

    2.718281828459045
    


```python
print(math.tau) 
```

    6.283185307179586
    


```python
print(math.inf) 
```

    inf
    


```python
print(math.nan)
```

    nan
    


```python
print(math.isfinite(math.nan)) 
```

    False
    


```python
print(math.isinf(-math.inf)) 
```

    True
    


```python
print(math.isnan(0))
```

    False
    


```python
r = 3
print(math.pi * r**2)
```

    28.274333882308138
    


```python
print(math.tau * r) 
```

    18.84955592153876
    


```python
deg = 60
rad = math.radians(deg)
print(math.degrees(rad))
```

    59.99999999999999
    


```python
print(math.hypot(3, 4, 12))
```

    13.0
    


```python
print(math.atan2(1, 0))
```

    1.5707963267948966
    


```python
print(math.atan2(-1, 0))
```

    -1.5707963267948966
    


```python
print(math.tau / 2)
```

    3.141592653589793
    


```python
r = 5
print((math.pi * r ** 2) / 2)
```

    39.269908169872416
    


```python
print(math.isclose(1.001, 1.002, abs_tol=0.01)) 
```

    True
    


```python
print(math.e ** 2)
```

    7.3890560989306495
    


```python
print(math.log(math.e))
```

    1.0
    


```python
print(math.radians(0))
```

    0.0
    


```python
print(math.factorial(5)) 
```

    120
    


```python
print(math.factorial(0))
```

    1
    


```python
print(math.factorial(1))
```

    1
    


```python
print(math.comb(5, 2))
```

    10
    


```python
print(math.comb(4, 4)) 
```

    1
    


```python
print(math.comb(6, 0))
```

    1
    


```python
print(math.perm(5, 2)) 
```

    20
    


```python
print(math.perm(4, 4)) 
```

    24
    


```python
print(math.perm(7, 0)) 
```

    1
    


```python
print(math.gamma(5))
```

    24.0
    


```python

print(math.gamma(2.5))
```

    1.3293403881791372
    


```python
print(math.lgamma(5))
```

    3.178053830347945
    


```python
print(math.lgamma(1)) 
```

    0.0
    


```python
print(math.gamma(0.5))

```

    1.7724538509055159
    


```python
print(math.lgamma(0.5))
```

    0.5723649429247004
    


```python
print(math.factorial(10)) 
```

    3628800
    


```python
print(math.comb(10, 3))
```

    120
    


```python
print(math.perm(10, 3))
```

    720
    


```python
print(math.gamma(1)) 
```

    1.0
    


```python
print(math.gamma(2)) 
```

    1.0
    


```python
print(math.gamma(3))
```

    2.0
    


```python
print(math.gamma(4))
```

    6.0
    


```python
print(math.lgamma(2)) 
```

    0.0
    


```python
print(math.comb(20, 10))  
```

    184756
    


```python
print(math.perm(8, 5))
```

    6720
    


```python
print(round(math.gamma(4.5), 2)) 
```

    11.63
    


```python
print(round(math.lgamma(4.5), 2)) 
```

    2.45
    


```python
try:
    print(math.factorial(-5))
except ValueError:
    print("Negative factorial error")
```

    Negative factorial error
    


```python
try:
    print(math.comb(4, 5))
except ValueError:
    print("k > n error")

```

    0
    


```python
try:
    print(math.perm(4, 5))
except ValueError:
    print("k > n error")

```

    0
    


```python
#Advanced, Nested, and Composed Usage 
```


```python
x = math.pi / 4
print(round(math.sin(x)**2 + math.cos(x)**2, 5))  # 1.0

```

    1.0
    


```python
a, b, c = 1, -3, 2
root1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
print(root1)
```

    2.0
    


```python
v = (3, 4)
print(math.hypot(*v))  # 5.0
```

    5.0
    


```python
deg = 75
print(math.degrees(math.radians(deg)))  # 75.0
```

    75.0
    


```python
dx = 4
dy = 3
print(math.degrees(math.atan2(dy, dx)))  # 36.87...
```

    36.86989764584402
    


```python
x = 1.5
print(1 / (1 + math.exp(-x)))
```

    0.8175744761936437
    


```python
a, b = 100, 10
print(math.log(a) / math.log(b))  # log base 10
```

    2.0
    


```python
a, b, c = 5, 5, 6
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(area)
```

    12.0
    


```python
A0, k, t = 100, 0.1, 5
print(A0 * math.exp(-k * t))
```

    60.653065971263345
    


```python
P, r, n, t = 1000, 0.05, 12, 10
print(P * math.pow(1 + r/n, n*t))
```

    1647.00949769028
    


```python
print(math.sin(math.radians(30)))  # 0.5
```

    0.49999999999999994
    


```python
print(math.atan2(-3, -3))
```

    -2.356194490192345
    


```python
print(math.hypot(3, 4, 12)) 
```

    13.0
    


```python
angle = -3
print((angle + 2 * math.pi) % (2 * math.pi))
```

    3.2831853071795862
    


```python
d = 30
r = math.radians(d)
s = math.sin(r)
print(s)
```

    0.49999999999999994
    


```python
x = math.pi / 3
print((math.sin(x) + math.cos(x)) / 2)

```

    0.6830127018922194
    


```python
decimal, whole = math.modf(3.75)
print(whole, decimal)
```

    3.0 0.75
    


```python
x = 1e-10
print(math.log1p(x))
```

    9.999999999500001e-11
    


```python
print(math.expm1(x))
```

    1.00000000005e-10
    


```python
a, b = 4, 6
print(2 * a * b / (a + b))
```

    4.8
    


```python
a, b = 4, 9
print(math.sqrt(a * b))
```

    6.0
    


```python
r = 10
theta = math.radians(60)
print(r * theta)
```

    10.471975511965976
    


```python
print(0.5 * r**2 * theta)

```

    52.35987755982988
    


```python
print(math.sin(math.tau))  # ~0
print(math.cos(math.tau))  # ~1
```

    -2.4492935982947064e-16
    1.0
    


```python
a, b = 10, 0
try:
    result = a / b
    print(math.isfinite(result))
except ZeroDivisionError:
    print("Divide by zero!")
```

    Divide by zero!
    


```python
x, min_x, max_x = 7, 5, 15
print((x - min_x) / (max_x - min_x))

```

    0.2
    


```python
print(((x - min_x) / (max_x - min_x)) * 100)
```

    20.0
    


```python
r, theta = 5, math.radians(60)
x = r * math.cos(theta)
y = r * math.sin(theta)
print(x, y)
```

    2.5000000000000004 4.330127018922193
    


```python
r = math.hypot(x, y)
theta = math.degrees(math.atan2(y, x))
print(r, theta)

```

    5.0 59.99999999999999
    


```python
a, b, angle = 3, 4, math.radians(90)
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle))
print(c)  # Should be 5
```

    5.0
    


```python

```


---
**Score: 185**