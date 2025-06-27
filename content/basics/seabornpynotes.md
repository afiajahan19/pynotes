---
title: Seabornpynotes
date: 2025-06-27
author: Your Name
cell_count: 11
score: 10
---

```python
# Install and check seaborn version
!pip show seaborn | grep "Version:"
# Output: Version: 0.13.2

import matplotlib.pyplot as plt
import seaborn as sns

# Set seaborn theme
sns.set_theme(style="darkgrid")

# Simple line plot with just x values
x = [0, 220, 380, 500, 540, 540, 590]
sns.lineplot(x=x)
plt.title("Basic Line Plot")
plt.show()

```

    'grep' is not recognized as an internal or external command,
    operable program or batch file.
    


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    Cell In[1], line 5
          2 get_ipython().system('pip show seaborn | grep "Version:"')
          3 # Output: Version: 0.13.2
    ----> 5 import matplotlib.pyplot as plt
          6 import seaborn as sns
          8 # Set seaborn theme
    

    ModuleNotFoundError: No module named 'matplotlib'



```python
!pip install matplotlib seaborn

```

    Collecting matplotlib
      Downloading matplotlib-3.10.3-cp312-cp312-win_amd64.whl.metadata (11 kB)
    Collecting seaborn
      Downloading seaborn-0.13.2-py3-none-any.whl.metadata (5.4 kB)
    Collecting contourpy>=1.0.1 (from matplotlib)
      Downloading contourpy-1.3.2-cp312-cp312-win_amd64.whl.metadata (5.5 kB)
    Collecting cycler>=0.10 (from matplotlib)
      Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
    Collecting fonttools>=4.22.0 (from matplotlib)
      Downloading fonttools-4.58.4-cp312-cp312-win_amd64.whl.metadata (108 kB)
    Collecting kiwisolver>=1.3.1 (from matplotlib)
      Downloading kiwisolver-1.4.8-cp312-cp312-win_amd64.whl.metadata (6.3 kB)
    Requirement already satisfied: numpy>=1.23 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib) (2.3.1)
    Requirement already satisfied: packaging>=20.0 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib) (25.0)
    Collecting pillow>=8 (from matplotlib)
      Downloading pillow-11.2.1-cp312-cp312-win_amd64.whl.metadata (9.1 kB)
    Collecting pyparsing>=2.3.1 (from matplotlib)
      Downloading pyparsing-3.2.3-py3-none-any.whl.metadata (5.0 kB)
    Requirement already satisfied: python-dateutil>=2.7 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib) (2.9.0.post0)
    Requirement already satisfied: pandas>=1.2 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from seaborn) (2.3.0)
    Requirement already satisfied: pytz>=2020.1 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from pandas>=1.2->seaborn) (2025.2)
    Requirement already satisfied: tzdata>=2022.7 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from pandas>=1.2->seaborn) (2025.2)
    Requirement already satisfied: six>=1.5 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from python-dateutil>=2.7->matplotlib) (1.17.0)
    Downloading matplotlib-3.10.3-cp312-cp312-win_amd64.whl (8.1 MB)
       ---------------------------------------- 0.0/8.1 MB ? eta -:--:--
       ---------------------------------------- 0.0/8.1 MB ? eta -:--:--
       - -------------------------------------- 0.3/8.1 MB ? eta -:--:--
       --- ------------------------------------ 0.8/8.1 MB 1.3 MB/s eta 0:00:06
       ----- ---------------------------------- 1.0/8.1 MB 1.6 MB/s eta 0:00:05
       ------- -------------------------------- 1.6/8.1 MB 1.8 MB/s eta 0:00:04
       ---------- ----------------------------- 2.1/8.1 MB 2.0 MB/s eta 0:00:04
       -------------- ------------------------- 2.9/8.1 MB 2.1 MB/s eta 0:00:03
       --------------- ------------------------ 3.1/8.1 MB 2.1 MB/s eta 0:00:03
       ------------------- -------------------- 3.9/8.1 MB 2.2 MB/s eta 0:00:02
       -------------------- ------------------- 4.2/8.1 MB 2.2 MB/s eta 0:00:02
       ------------------------ --------------- 5.0/8.1 MB 2.3 MB/s eta 0:00:02
       --------------------------- ------------ 5.5/8.1 MB 2.3 MB/s eta 0:00:02
       ----------------------------- ---------- 6.0/8.1 MB 2.3 MB/s eta 0:00:01
       -------------------------------- ------- 6.6/8.1 MB 2.3 MB/s eta 0:00:01
       ----------------------------------- ---- 7.1/8.1 MB 2.3 MB/s eta 0:00:01
       ------------------------------------- -- 7.6/8.1 MB 2.4 MB/s eta 0:00:01
       -------------------------------------- - 7.9/8.1 MB 2.4 MB/s eta 0:00:01
       ---------------------------------------- 8.1/8.1 MB 2.3 MB/s eta 0:00:00
    Downloading seaborn-0.13.2-py3-none-any.whl (294 kB)
    Downloading contourpy-1.3.2-cp312-cp312-win_amd64.whl (223 kB)
    Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
    Downloading fonttools-4.58.4-cp312-cp312-win_amd64.whl (2.2 MB)
       ---------------------------------------- 0.0/2.2 MB ? eta -:--:--
       ---- ----------------------------------- 0.3/2.2 MB ? eta -:--:--
       -------------- ------------------------- 0.8/2.2 MB 2.4 MB/s eta 0:00:01
       ---------------------------- ----------- 1.6/2.2 MB 2.5 MB/s eta 0:00:01
       ------------------------------------- -- 2.1/2.2 MB 2.5 MB/s eta 0:00:01
       ---------------------------------------- 2.2/2.2 MB 2.4 MB/s eta 0:00:00
    Downloading kiwisolver-1.4.8-cp312-cp312-win_amd64.whl (71 kB)
    Downloading pillow-11.2.1-cp312-cp312-win_amd64.whl (2.7 MB)
       ---------------------------------------- 0.0/2.7 MB ? eta -:--:--
       ------- -------------------------------- 0.5/2.7 MB 2.4 MB/s eta 0:00:01
       --------------- ------------------------ 1.0/2.7 MB 2.4 MB/s eta 0:00:01
       ------------------- -------------------- 1.3/2.7 MB 2.3 MB/s eta 0:00:01
       --------------------------- ------------ 1.8/2.7 MB 2.3 MB/s eta 0:00:01
       ----------------------------------- ---- 2.4/2.7 MB 2.4 MB/s eta 0:00:01
       ---------------------------------------- 2.7/2.7 MB 2.2 MB/s eta 0:00:00
    Downloading pyparsing-3.2.3-py3-none-any.whl (111 kB)
    Installing collected packages: pyparsing, pillow, kiwisolver, fonttools, cycler, contourpy, matplotlib, seaborn
    
       ---------------------------------------- 0/8 [pyparsing]
       ---------------------------------------- 0/8 [pyparsing]
       ----- ---------------------------------- 1/8 [pillow]
       ----- ---------------------------------- 1/8 [pillow]
       ----- ---------------------------------- 1/8 [pillow]
       ----- ---------------------------------- 1/8 [pillow]
       ----- ---------------------------------- 1/8 [pillow]
       ----- ---------------------------------- 1/8 [pillow]
       ----- ---------------------------------- 1/8 [pillow]
       ----- ---------------------------------- 1/8 [pillow]
       ----- ---------------------------------- 1/8 [pillow]
       ----- ---------------------------------- 1/8 [pillow]
       ---------- ----------------------------- 2/8 [kiwisolver]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       --------------- ------------------------ 3/8 [fonttools]
       ------------------------- -------------- 5/8 [contourpy]
       ------------------------- -------------- 5/8 [contourpy]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ------------------------------ --------- 6/8 [matplotlib]
       ----------------------------------- ---- 7/8 [seaborn]
       ----------------------------------- ---- 7/8 [seaborn]
       ----------------------------------- ---- 7/8 [seaborn]
       ----------------------------------- ---- 7/8 [seaborn]
       ----------------------------------- ---- 7/8 [seaborn]
       ----------------------------------- ---- 7/8 [seaborn]
       ---------------------------------------- 8/8 [seaborn]
    
    Successfully installed contourpy-1.3.2 cycler-0.12.1 fonttools-4.58.4 kiwisolver-1.4.8 matplotlib-3.10.3 pillow-11.2.1 pyparsing-3.2.3 seaborn-0.13.2
    


```python
import seaborn as sns
print("Seaborn version:", sns.__version__)

```

    Matplotlib is building the font cache; this may take a moment.
    

    Seaborn version: 0.13.2
    


```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")

x = [0, 220, 380, 500, 540, 540, 590]

sns.lineplot(x=x)
plt.title("Basic Line Plot")
plt.show()

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\indexes\base.py:3812, in Index.get_loc(self, key)
       3811 try:
    -> 3812     return self._engine.get_loc(casted_key)
       3813 except KeyError as err:
    

    File pandas/_libs/index.pyx:167, in pandas._libs.index.IndexEngine.get_loc()
    

    File pandas/_libs/index.pyx:196, in pandas._libs.index.IndexEngine.get_loc()
    

    File pandas/_libs/hashtable_class_helper.pxi:7088, in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    File pandas/_libs/hashtable_class_helper.pxi:7096, in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: 'y'

    
    The above exception was the direct cause of the following exception:
    

    KeyError                                  Traceback (most recent call last)

    Cell In[4], line 8
          4 sns.set_theme(style="darkgrid")
          6 x = [0, 220, 380, 500, 540, 540, 590]
    ----> 8 sns.lineplot(x=x)
          9 plt.title("Basic Line Plot")
         10 plt.show()
    

    File ~\anaconda3\envs\py312\Lib\site-packages\seaborn\relational.py:515, in lineplot(data, x, y, hue, size, style, units, weights, palette, hue_order, hue_norm, sizes, size_order, size_norm, dashes, markers, style_order, estimator, errorbar, n_boot, seed, orient, sort, err_style, err_kws, legend, ci, ax, **kwargs)
        512 color = kwargs.pop("color", kwargs.pop("c", None))
        513 kwargs["color"] = _default_color(ax.plot, hue, color, kwargs)
    --> 515 p.plot(ax, kwargs)
        516 return ax
    

    File ~\anaconda3\envs\py312\Lib\site-packages\seaborn\relational.py:295, in _LinePlotter.plot(self, ax, kws)
        291     grouped = sub_data.groupby(orient, sort=self.sort)
        292     # Could pass as_index=False instead of reset_index,
        293     # but that fails on a corner case with older pandas.
        294     sub_data = (
    --> 295         grouped
        296         .apply(agg, other, **groupby_apply_include_groups(False))
        297         .reset_index()
        298     )
        299 else:
        300     sub_data[f"{other}min"] = np.nan
    

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\groupby\groupby.py:1819, in GroupBy.apply(self, func, include_groups, *args, **kwargs)
       1816     f = func
       1818 if not include_groups:
    -> 1819     return self._python_apply_general(f, self._obj_with_exclusions)
       1821 # ignore SettingWithCopy here in case the user mutates
       1822 with option_context("mode.chained_assignment", None):
    

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\groupby\groupby.py:1885, in GroupBy._python_apply_general(self, f, data, not_indexed_same, is_transform, is_agg)
       1850 @final
       1851 def _python_apply_general(
       1852     self,
       (...)   1857     is_agg: bool = False,
       1858 ) -> NDFrameT:
       1859     """
       1860     Apply function f in python space
       1861 
       (...)   1883         data after applying f
       1884     """
    -> 1885     values, mutated = self._grouper.apply_groupwise(f, data, self.axis)
       1886     if not_indexed_same is None:
       1887         not_indexed_same = mutated
    

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\groupby\ops.py:919, in BaseGrouper.apply_groupwise(self, f, data, axis)
        917 # group might be modified
        918 group_axes = group.axes
    --> 919 res = f(group)
        920 if not mutated and not _is_indexed_like(res, group_axes, axis):
        921     mutated = True
    

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\groupby\groupby.py:1809, in GroupBy.apply.<locals>.f(g)
       1807 @wraps(func)
       1808 def f(g):
    -> 1809     return func(g, *args, **kwargs)
    

    File ~\anaconda3\envs\py312\Lib\site-packages\seaborn\_statistics.py:486, in EstimateAggregator.__call__(self, data, var)
        484 def __call__(self, data, var):
        485     """Aggregate over `var` column of `data` with estimate and error interval."""
    --> 486     vals = data[var]
        487     if callable(self.estimator):
        488         # You would think we could pass to vals.agg, and yet:
        489         # https://github.com/mwaskom/seaborn/issues/2943
        490         estimate = self.estimator(vals)
    

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\frame.py:4107, in DataFrame.__getitem__(self, key)
       4105 if self.columns.nlevels > 1:
       4106     return self._getitem_multilevel(key)
    -> 4107 indexer = self.columns.get_loc(key)
       4108 if is_integer(indexer):
       4109     indexer = [indexer]
    

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\indexes\base.py:3819, in Index.get_loc(self, key)
       3814     if isinstance(casted_key, slice) or (
       3815         isinstance(casted_key, abc.Iterable)
       3816         and any(isinstance(x, slice) for x in casted_key)
       3817     ):
       3818         raise InvalidIndexError(key)
    -> 3819     raise KeyError(key) from err
       3820 except TypeError:
       3821     # If we have a listlike key, _check_indexing_error will raise
       3822     #  InvalidIndexError. Otherwise we fall through and re-raise
       3823     #  the TypeError.
       3824     self._check_indexing_error(key)
    

    KeyError: 'y'



    
![png](/pynotes/images/seabornpynotes_3_1.png)
    



```python
import pandas as pd

# Data
days_list = [1, 1, 1, 2, 2, 2, 3, 3, 3]
learners_list = ['raja', 'hari', 'steve', 'raja', 'hari', 'steve', 'raja', 'hari', 'steve']
score_list = [0, 0, 0, 50, 40, 60, 60, 45, 60]

data = {
    'days': days_list,
    'learners': learners_list,
    'score': score_list
}

# DataFrame
df = pd.DataFrame(data)

# Convert to wide format
df_wide = df.pivot(index="days", columns="learners", values="score")

# Plot
sns.lineplot(data=df_wide)
plt.title("Learners' Score Over Days")
plt.xlabel("Days")
plt.ylabel("Score")
plt.show()

```


```python
!pip install matplotlib seaborn

```

    Requirement already satisfied: matplotlib in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (3.10.3)
    Requirement already satisfied: seaborn in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (0.13.2)
    Requirement already satisfied: contourpy>=1.0.1 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib) (1.3.2)
    Requirement already satisfied: cycler>=0.10 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib) (0.12.1)
    Requirement already satisfied: fonttools>=4.22.0 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib) (4.58.4)
    Requirement already satisfied: kiwisolver>=1.3.1 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib) (1.4.8)
    Requirement already satisfied: numpy>=1.23 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib) (2.3.1)
    Requirement already satisfied: packaging>=20.0 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib) (25.0)
    Requirement already satisfied: pillow>=8 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib) (11.2.1)
    Requirement already satisfied: pyparsing>=2.3.1 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib) (3.2.3)
    Requirement already satisfied: python-dateutil>=2.7 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from matplotlib) (2.9.0.post0)
    Requirement already satisfied: pandas>=1.2 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from seaborn) (2.3.0)
    Requirement already satisfied: pytz>=2020.1 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from pandas>=1.2->seaborn) (2025.2)
    Requirement already satisfied: tzdata>=2022.7 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from pandas>=1.2->seaborn) (2025.2)
    Requirement already satisfied: six>=1.5 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from python-dateutil>=2.7->matplotlib) (1.17.0)
    


```python
import seaborn as sns
print("Seaborn version:", sns.__version__)

```

    Seaborn version: 0.13.2
    


```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")

x = [0, 220, 380, 500, 540, 540, 590]

sns.lineplot(x=x)
plt.title("Basic Line Plot")
plt.show()

```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\indexes\base.py:3812, in Index.get_loc(self, key)
       3811 try:
    -> 3812     return self._engine.get_loc(casted_key)
       3813 except KeyError as err:
    

    File pandas/_libs/index.pyx:167, in pandas._libs.index.IndexEngine.get_loc()
    

    File pandas/_libs/index.pyx:196, in pandas._libs.index.IndexEngine.get_loc()
    

    File pandas/_libs/hashtable_class_helper.pxi:7088, in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    File pandas/_libs/hashtable_class_helper.pxi:7096, in pandas._libs.hashtable.PyObjectHashTable.get_item()
    

    KeyError: 'y'

    
    The above exception was the direct cause of the following exception:
    

    KeyError                                  Traceback (most recent call last)

    Cell In[7], line 8
          4 sns.set_theme(style="darkgrid")
          6 x = [0, 220, 380, 500, 540, 540, 590]
    ----> 8 sns.lineplot(x=x)
          9 plt.title("Basic Line Plot")
         10 plt.show()
    

    File ~\anaconda3\envs\py312\Lib\site-packages\seaborn\relational.py:515, in lineplot(data, x, y, hue, size, style, units, weights, palette, hue_order, hue_norm, sizes, size_order, size_norm, dashes, markers, style_order, estimator, errorbar, n_boot, seed, orient, sort, err_style, err_kws, legend, ci, ax, **kwargs)
        512 color = kwargs.pop("color", kwargs.pop("c", None))
        513 kwargs["color"] = _default_color(ax.plot, hue, color, kwargs)
    --> 515 p.plot(ax, kwargs)
        516 return ax
    

    File ~\anaconda3\envs\py312\Lib\site-packages\seaborn\relational.py:295, in _LinePlotter.plot(self, ax, kws)
        291     grouped = sub_data.groupby(orient, sort=self.sort)
        292     # Could pass as_index=False instead of reset_index,
        293     # but that fails on a corner case with older pandas.
        294     sub_data = (
    --> 295         grouped
        296         .apply(agg, other, **groupby_apply_include_groups(False))
        297         .reset_index()
        298     )
        299 else:
        300     sub_data[f"{other}min"] = np.nan
    

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\groupby\groupby.py:1819, in GroupBy.apply(self, func, include_groups, *args, **kwargs)
       1816     f = func
       1818 if not include_groups:
    -> 1819     return self._python_apply_general(f, self._obj_with_exclusions)
       1821 # ignore SettingWithCopy here in case the user mutates
       1822 with option_context("mode.chained_assignment", None):
    

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\groupby\groupby.py:1885, in GroupBy._python_apply_general(self, f, data, not_indexed_same, is_transform, is_agg)
       1850 @final
       1851 def _python_apply_general(
       1852     self,
       (...)   1857     is_agg: bool = False,
       1858 ) -> NDFrameT:
       1859     """
       1860     Apply function f in python space
       1861 
       (...)   1883         data after applying f
       1884     """
    -> 1885     values, mutated = self._grouper.apply_groupwise(f, data, self.axis)
       1886     if not_indexed_same is None:
       1887         not_indexed_same = mutated
    

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\groupby\ops.py:919, in BaseGrouper.apply_groupwise(self, f, data, axis)
        917 # group might be modified
        918 group_axes = group.axes
    --> 919 res = f(group)
        920 if not mutated and not _is_indexed_like(res, group_axes, axis):
        921     mutated = True
    

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\groupby\groupby.py:1809, in GroupBy.apply.<locals>.f(g)
       1807 @wraps(func)
       1808 def f(g):
    -> 1809     return func(g, *args, **kwargs)
    

    File ~\anaconda3\envs\py312\Lib\site-packages\seaborn\_statistics.py:486, in EstimateAggregator.__call__(self, data, var)
        484 def __call__(self, data, var):
        485     """Aggregate over `var` column of `data` with estimate and error interval."""
    --> 486     vals = data[var]
        487     if callable(self.estimator):
        488         # You would think we could pass to vals.agg, and yet:
        489         # https://github.com/mwaskom/seaborn/issues/2943
        490         estimate = self.estimator(vals)
    

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\frame.py:4107, in DataFrame.__getitem__(self, key)
       4105 if self.columns.nlevels > 1:
       4106     return self._getitem_multilevel(key)
    -> 4107 indexer = self.columns.get_loc(key)
       4108 if is_integer(indexer):
       4109     indexer = [indexer]
    

    File ~\anaconda3\envs\py312\Lib\site-packages\pandas\core\indexes\base.py:3819, in Index.get_loc(self, key)
       3814     if isinstance(casted_key, slice) or (
       3815         isinstance(casted_key, abc.Iterable)
       3816         and any(isinstance(x, slice) for x in casted_key)
       3817     ):
       3818         raise InvalidIndexError(key)
    -> 3819     raise KeyError(key) from err
       3820 except TypeError:
       3821     # If we have a listlike key, _check_indexing_error will raise
       3822     #  InvalidIndexError. Otherwise we fall through and re-raise
       3823     #  the TypeError.
       3824     self._check_indexing_error(key)
    

    KeyError: 'y'



    
![png](/pynotes/images/seabornpynotes_7_1.png)
    



```python
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")

x = [0, 1, 2, 3, 4, 5, 6]  # indices
y = [0, 220, 380, 500, 540, 540, 590]

sns.lineplot(x=x, y=y)
plt.title("Basic Line Plot")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()

```


    
![png](/pynotes/images/seabornpynotes_8_0.png)
    



```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = {
    'days': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    'learners': ['raja', 'hari', 'steve', 'raja', 'hari', 'steve', 'raja', 'hari', 'steve'],
    'score': [0, 0, 0, 50, 40, 60, 60, 45, 60]
}

df = pd.DataFrame(data)

# Pivot table to get multiple series (columns per learner)
df_wide = df.pivot(index="days", columns="learners", values="score")

# Plot all learners in one line plot
sns.lineplot(data=df_wide)
plt.title("Multiple Learners' Score Over Days")
plt.xlabel("Days")
plt.ylabel("Score")
plt.show()

```


    
![png](/pynotes/images/seabornpynotes_9_0.png)
    



```python

```


---
**Score: 10**