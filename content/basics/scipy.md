---
title: Scipy
date: 2025-06-29
author: Your Name
cell_count: 55
score: 55
---

```python
# 1. Import scipy
import scipy
print("SciPy version:", scipy.__version__)

```

    SciPy version: 1.13.1
    


```python
# 2. Use scipy.constants to get pi
from scipy.constants import pi
print("Value of pi:", pi)

```

    Value of pi: 3.141592653589793
    


```python
# 3. Speed of light
from scipy.constants import c
print("Speed of light (m/s):", c)

```

    Speed of light (m/s): 299792458.0
    


```python
# 4. Planck’s constant
from scipy.constants import h
print("Planck’s constant:", h)

```

    Planck’s constant: 6.62607015e-34
    


```python
# 5. Gravitational constant
from scipy.constants import G
print("Gravitational constant:", G)

```

    Gravitational constant: 6.6743e-11
    


```python
# 6. Boltzmann constant
from scipy.constants import k
print("Boltzmann constant:", k)

```

    Boltzmann constant: 1.380649e-23
    


```python
# 7. Avogadro constant
from scipy.constants import N_A
print("Avogadro's number:", N_A)

```

    Avogadro's number: 6.02214076e+23
    


```python
# 8. Electron charge
from scipy.constants import e
print("Elementary charge:", e)

```

    Elementary charge: 1.602176634e-19
    


```python
# 9. Vacuum permittivity
from scipy.constants import epsilon_0
print("Vacuum permittivity:", epsilon_0)

```

    Vacuum permittivity: 8.8541878128e-12
    


```python
# 10. Convert calories to joules
from scipy.constants import calorie
print("1 calorie = ", calorie, "Joules")

```

    1 calorie =  4.184 Joules
    


```python
# 11. Convert hour to seconds
from scipy.constants import hour
print("1 hour =", hour, "seconds")

```

    1 hour = 3600.0 seconds
    


```python
# 12. Convert inches to meters
from scipy.constants import inch
print("1 inch =", inch, "meters")

```

    1 inch = 0.0254 meters
    


```python
# 13. Convert miles to meters
from scipy.constants import mile
print("1 mile =", mile, "meters")

```

    1 mile = 1609.3439999999998 meters
    


```python
# 14. Convert degree to radians
from scipy.constants import degree
print("1 degree =", degree, "radians")

```

    1 degree = 0.017453292519943295 radians
    


```python
# 15. List all available physical constants
import scipy.constants
print(dir(scipy.constants))

```

    ['Avogadro', 'Boltzmann', 'Btu', 'Btu_IT', 'Btu_th', 'ConstantWarning', 'G', 'Julian_year', 'N_A', 'Planck', 'R', 'Rydberg', 'Stefan_Boltzmann', 'Wien', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_codata', '_constants', '_obsolete_constants', 'acre', 'alpha', 'angstrom', 'arcmin', 'arcminute', 'arcsec', 'arcsecond', 'astronomical_unit', 'atm', 'atmosphere', 'atomic_mass', 'atto', 'au', 'bar', 'barrel', 'bbl', 'blob', 'c', 'calorie', 'calorie_IT', 'calorie_th', 'carat', 'centi', 'codata', 'constants', 'convert_temperature', 'day', 'deci', 'degree', 'degree_Fahrenheit', 'deka', 'dyn', 'dyne', 'e', 'eV', 'electron_mass', 'electron_volt', 'elementary_charge', 'epsilon_0', 'erg', 'exa', 'exbi', 'femto', 'fermi', 'find', 'fine_structure', 'fluid_ounce', 'fluid_ounce_US', 'fluid_ounce_imp', 'foot', 'g', 'gallon', 'gallon_US', 'gallon_imp', 'gas_constant', 'gibi', 'giga', 'golden', 'golden_ratio', 'grain', 'gram', 'gravitational_constant', 'h', 'hbar', 'hectare', 'hecto', 'horsepower', 'hour', 'hp', 'inch', 'k', 'kgf', 'kibi', 'kilo', 'kilogram_force', 'kmh', 'knot', 'lambda2nu', 'lb', 'lbf', 'light_year', 'liter', 'litre', 'long_ton', 'm_e', 'm_n', 'm_p', 'm_u', 'mach', 'mebi', 'mega', 'metric_ton', 'micro', 'micron', 'mil', 'mile', 'milli', 'minute', 'mmHg', 'mph', 'mu_0', 'nano', 'nautical_mile', 'neutron_mass', 'nu2lambda', 'ounce', 'oz', 'parsec', 'pebi', 'peta', 'physical_constants', 'pi', 'pico', 'point', 'pound', 'pound_force', 'precision', 'proton_mass', 'psi', 'pt', 'quecto', 'quetta', 'ronna', 'ronto', 'short_ton', 'sigma', 'slinch', 'slug', 'speed_of_light', 'speed_of_sound', 'stone', 'survey_foot', 'survey_mile', 'tebi', 'tera', 'test', 'ton_TNT', 'torr', 'troy_ounce', 'troy_pound', 'u', 'unit', 'value', 'week', 'yard', 'year', 'yobi', 'yocto', 'yotta', 'zebi', 'zepto', 'zero_Celsius', 'zetta']
    


```python
# 16. Find value of golden ratio
from scipy.constants import golden
print("Golden Ratio:", golden)

```

    Golden Ratio: 1.618033988749895
    


```python
# 17. Find standard acceleration due to gravity
from scipy.constants import g
print("Standard gravity:", g)

```

    Standard gravity: 9.80665
    


```python
# 18. Find molar gas constant
from scipy.constants import R
print("Molar gas constant:", R)

```

    Molar gas constant: 8.314462618
    


```python
# 19. Find Stefan-Boltzmann constant
from scipy.constants import sigma
print("Stefan-Boltzmann constant:", sigma)

```

    Stefan-Boltzmann constant: 5.670374419e-08
    


```python
# 20. Convert mmHg to Pascal
from scipy.constants import mmHg
print("1 mmHg =", mmHg, "Pascal")

```

    1 mmHg = 133.32236842105263 Pascal
    


```python
# 21. Gamma function
from scipy.special import gamma
print("Gamma(5):", gamma(5))

```

    Gamma(5): 24.0
    


```python
# 22. Factorial using gamma
print("Factorial(4):", gamma(5))  # gamma(n+1) = n!

```

    Factorial(4): 24.0
    


```python
# 23. Log gamma function
from scipy.special import gammaln
print("Log Gamma(10):", gammaln(10))

```

    Log Gamma(10): 12.801827480081469
    


```python
# 24. Beta function
from scipy.special import beta
print("Beta(2, 3):", beta(2, 3))

```

    Beta(2, 3): 0.08333333333333333
    


```python
from scipy.special import erf
print("erf(1):", erf(1))
```

    erf(1): 0.8427007929497148
    


```python
# 26. Complementary error function
from scipy.special import erfc
print("erfc(1):", erfc(1))

```

    erfc(1): 0.15729920705028516
    


```python
# 27. Exponential integral
from scipy.special import expi
print("Exponential integral of 1:", expi(1))

```

    Exponential integral of 1: 1.8951178163559368
    


```python
# 28. Bessel function of first kind (J0)
from scipy.special import j0
print("Bessel J0(1):", j0(1))


```

    Bessel J0(1): 0.7651976865579665
    


```python
# 29. Bessel function of second kind (Y0)
from scipy.special import y0
print("Bessel Y0(1):", y0(1))

```

    Bessel Y0(1): 0.08825696421567697
    


```python
# 30. Modified Bessel function of first kind (I0)
from scipy.special import i0
print("Modified Bessel I0(1):", i0(1))


```

    Modified Bessel I0(1): 1.2660658777520082
    


```python
# 31. Modified Bessel function of second kind (K0)
from scipy.special import k0
print("Modified Bessel K0(1):", k0(1))

```

    Modified Bessel K0(1): 0.42102443824070823
    


```python
# 34. Spherical Bessel function of first kind
from scipy.special import spherical_jn
print("spherical_jn(n=1, x=2):", spherical_jn(1, 2))


```

    spherical_jn(n=1, x=2): 0.43539777497999166
    


```python
# 35. Spherical Neumann function (second kind)
from scipy.special import spherical_yn
print("spherical_yn(n=1, x=2):", spherical_yn(1, 2))

```

    spherical_yn(n=1, x=2): -0.35061200427605527
    


```python
# 36. Legendre polynomial of degree 3
from scipy.special import legendre
print("Legendre polynomial P3(x):", legendre(3))

```

    Legendre polynomial P3(x):      3
    2.5 x - 1.5 x
    


```python
# 37. Hermite polynomial of degree 4
from scipy.special import hermite
print("Hermite polynomial H4(x):", hermite(4))

```

    Hermite polynomial H4(x):     4      2
    16 x - 48 x - 8.882e-16 x + 12
    


```python
# 38. Laguerre polynomial of degree 2
from scipy.special import laguerre
print("Laguerre polynomial L2(x):", laguerre(2))

```

    Laguerre polynomial L2(x):      2
    0.5 x - 2 x + 1
    


```python
# 39. Chebyshev polynomial of first kind
from scipy.special import chebyt
print("Chebyshev polynomial T3(x):", chebyt(3))

```

    Chebyshev polynomial T3(x):    3
    4 x - 3 x
    


```python
# 40. Chebyshev polynomial of second kind
from scipy.special import chebyu
print("Chebyshev polynomial U3(x):", chebyu(3))

```

    Chebyshev polynomial U3(x):    3
    8 x - 4 x
    


```python
# 41. Definite integral of a function using quad
from scipy.integrate import quad
result, error = quad(lambda x: x**2, 0, 1)
print("∫x^2 from 0 to 1 =", result)

```

    ∫x^2 from 0 to 1 = 0.33333333333333337
    


```python
# 42. Integrate sin(x) from 0 to pi
import numpy as np
result, _ = quad(np.sin, 0, np.pi)
print("∫sin(x) from 0 to π =", result)

```

    ∫sin(x) from 0 to π = 2.0
    


```python
# 44. Integrate 1/x from 1 to 2
result, _ = quad(lambda x: 1/x, 1, 2)
print("∫1/x from 1 to 2 =", result)

```

    ∫1/x from 1 to 2 = 0.6931471805599454
    


```python
# 45. Integrate a function with known singularity
def f(x):
    return np.log(x)
result, _ = quad(f, 1e-5, 1)
print("∫log(x) from 0 to 1 =", result)

```

    ∫log(x) from 0 to 1 = -0.9998748707429328
    


```python
# 46. Multiple integrals using dblquad (double integral)
from scipy.integrate import dblquad
result, _ = dblquad(lambda x, y: x * y, 0, 1, lambda x: 0, lambda x: 1)
print("∬xy dx dy over unit square =", result)

```

    ∬xy dx dy over unit square = 0.24999999999999997
    


```python
# 47. Triple integral using tplquad
from scipy.integrate import tplquad
result, _ = tplquad(lambda x, y, z: x*y*z, 0, 1, lambda x: 0, lambda x: 1,
                    lambda x, y: 0, lambda x, y: 1)
print("∭xyz over unit cube =", result)

```

    ∭xyz over unit cube = 0.12499999999999999
    


```python
# 48. Integrate using fixed quadrature (quadrature points = 3)
from scipy.integrate import fixed_quad
result, _ = fixed_quad(lambda x: x**2, 0, 1, n=3)
print("∫x^2 from 0 to 1 using fixed_quad =", result)

```

    ∫x^2 from 0 to 1 using fixed_quad = 0.33333333333333337
    


```python
# 49. Integrate with infinite limits
result, _ = quad(lambda x: np.exp(-x**2), -np.inf, np.inf)
print("∫exp(-x^2) over all x =", result)

```

    ∫exp(-x^2) over all x = 1.7724538509055159
    


```python
# 50. Return error estimate with integration
res, err = quad(np.sin, 0, np.pi)
print("Integral:", res, " Error estimate:", err)

```

    Integral: 2.0  Error estimate: 2.220446049250313e-14
    


```python
# 54. Use nquad for n-dimensional integration
from scipy.integrate import nquad
result, _ = nquad(lambda x, y: x*y, [[0, 1], [0, 1]])
print("nquad ∫∫xy =", result)

```

    nquad ∫∫xy = 0.24999999999999997
    


```python
# 55. Integrate x^2 from 0 to 1 using trapz
from scipy.integrate import trapz
x = np.linspace(0, 1, 100)
y = x**2
result = trapz(y, x)
print("Trapz ∫x² from 0 to 1 =", result)

```

    Trapz ∫x² from 0 to 1 = 0.33335033840084355
    

    C:\Users\Afia Jahan\AppData\Local\Temp\ipykernel_69668\2335716571.py:5: DeprecationWarning: 'scipy.integrate.trapz' is deprecated in favour of 'scipy.integrate.trapezoid' and will be removed in SciPy 1.14.0
      result = trapz(y, x)
    


```python
# 56. Simpson’s rule for integration
from scipy.integrate import simpson
result = simpson(y, x)
print("Simpson ∫x² from 0 to 1 =", result)

```

    Simpson ∫x² from 0 to 1 = 0.3333333333333333
    

    C:\Users\Afia Jahan\AppData\Local\Temp\ipykernel_69668\1626733707.py:3: DeprecationWarning: You are passing x=[0.         0.01010101 0.02020202 0.03030303 0.04040404 0.05050505
     0.06060606 0.07070707 0.08080808 0.09090909 0.1010101  0.11111111
     0.12121212 0.13131313 0.14141414 0.15151515 0.16161616 0.17171717
     0.18181818 0.19191919 0.2020202  0.21212121 0.22222222 0.23232323
     0.24242424 0.25252525 0.26262626 0.27272727 0.28282828 0.29292929
     0.3030303  0.31313131 0.32323232 0.33333333 0.34343434 0.35353535
     0.36363636 0.37373737 0.38383838 0.39393939 0.4040404  0.41414141
     0.42424242 0.43434343 0.44444444 0.45454545 0.46464646 0.47474747
     0.48484848 0.49494949 0.50505051 0.51515152 0.52525253 0.53535354
     0.54545455 0.55555556 0.56565657 0.57575758 0.58585859 0.5959596
     0.60606061 0.61616162 0.62626263 0.63636364 0.64646465 0.65656566
     0.66666667 0.67676768 0.68686869 0.6969697  0.70707071 0.71717172
     0.72727273 0.73737374 0.74747475 0.75757576 0.76767677 0.77777778
     0.78787879 0.7979798  0.80808081 0.81818182 0.82828283 0.83838384
     0.84848485 0.85858586 0.86868687 0.87878788 0.88888889 0.8989899
     0.90909091 0.91919192 0.92929293 0.93939394 0.94949495 0.95959596
     0.96969697 0.97979798 0.98989899 1.        ] as a positional argument. Please change your invocation to use keyword arguments. From SciPy 1.14, passing these as positional arguments will result in an error.
      result = simpson(y, x)
    


```python
# 57. Compare trapz vs simpson
print("Trapz:", trapz(y, x))
print("Simpson:", simpson(y, x))

```

    Trapz: 0.33335033840084355
    Simpson: 0.3333333333333333
    

    C:\Users\Afia Jahan\AppData\Local\Temp\ipykernel_69668\3054771013.py:2: DeprecationWarning: 'scipy.integrate.trapz' is deprecated in favour of 'scipy.integrate.trapezoid' and will be removed in SciPy 1.14.0
      print("Trapz:", trapz(y, x))
    C:\Users\Afia Jahan\AppData\Local\Temp\ipykernel_69668\3054771013.py:3: DeprecationWarning: You are passing x=[0.         0.01010101 0.02020202 0.03030303 0.04040404 0.05050505
     0.06060606 0.07070707 0.08080808 0.09090909 0.1010101  0.11111111
     0.12121212 0.13131313 0.14141414 0.15151515 0.16161616 0.17171717
     0.18181818 0.19191919 0.2020202  0.21212121 0.22222222 0.23232323
     0.24242424 0.25252525 0.26262626 0.27272727 0.28282828 0.29292929
     0.3030303  0.31313131 0.32323232 0.33333333 0.34343434 0.35353535
     0.36363636 0.37373737 0.38383838 0.39393939 0.4040404  0.41414141
     0.42424242 0.43434343 0.44444444 0.45454545 0.46464646 0.47474747
     0.48484848 0.49494949 0.50505051 0.51515152 0.52525253 0.53535354
     0.54545455 0.55555556 0.56565657 0.57575758 0.58585859 0.5959596
     0.60606061 0.61616162 0.62626263 0.63636364 0.64646465 0.65656566
     0.66666667 0.67676768 0.68686869 0.6969697  0.70707071 0.71717172
     0.72727273 0.73737374 0.74747475 0.75757576 0.76767677 0.77777778
     0.78787879 0.7979798  0.80808081 0.81818182 0.82828283 0.83838384
     0.84848485 0.85858586 0.86868687 0.87878788 0.88888889 0.8989899
     0.90909091 0.91919192 0.92929293 0.93939394 0.94949495 0.95959596
     0.96969697 0.97979798 0.98989899 1.        ] as a positional argument. Please change your invocation to use keyword arguments. From SciPy 1.14, passing these as positional arguments will result in an error.
      print("Simpson:", simpson(y, x))
    


```python
# 58. Double integral with bounds depending on x
result, _ = dblquad(lambda x, y: x + y, 0, 2, lambda x: 0, lambda x: x)
print("∬(x+y) with y from 0 to x, x from 0 to 2 =", result)

```

    ∬(x+y) with y from 0 to x, x from 0 to 2 = 4.0
    


```python
# 59. Use tplquad with trigonometric function
result, _ = tplquad(lambda x, y, z: np.sin(x*y*z), 0, 1, lambda x: 0, lambda x: 1, lambda x, y: 0, lambda x, y: 1)
print("Triple integral of sin(x*y*z):", result)

```

    Triple integral of sin(x*y*z): 0.12243402879673786
    


```python
# 60. Integrate function with discontinuity
result, _ = quad(lambda x: np.piecewise(x, [x < 0.5, x >= 0.5], [1, 2]), 0, 1)
print("∫piecewise function from 0 to 1:", result)

```

    ∫piecewise function from 0 to 1: 1.5
    


```python

```


---
**Score: 55**