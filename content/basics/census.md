---
title: Census
date: 2025-06-29
author: Your Name
cell_count: 24
score: 20
---

```python
import pandas as pd

# Publicly available dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

# Define column names (from UCI description)
columns = [
    "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
    "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
    "hours-per-week", "native-country", "income"
]

# Read CSV with defined parameters
census = pd.read_csv(url, names=columns, na_values=" ?", skipinitialspace=True)

# Preview
print(census.head())

```

       age         workclass  fnlwgt  education  education-num  \
    0   39         State-gov   77516  Bachelors             13   
    1   50  Self-emp-not-inc   83311  Bachelors             13   
    2   38           Private  215646    HS-grad              9   
    3   53           Private  234721       11th              7   
    4   28           Private  338409  Bachelors             13   
    
           marital-status         occupation   relationship   race     sex  \
    0       Never-married       Adm-clerical  Not-in-family  White    Male   
    1  Married-civ-spouse    Exec-managerial        Husband  White    Male   
    2            Divorced  Handlers-cleaners  Not-in-family  White    Male   
    3  Married-civ-spouse  Handlers-cleaners        Husband  Black    Male   
    4  Married-civ-spouse     Prof-specialty           Wife  Black  Female   
    
       capital-gain  capital-loss  hours-per-week native-country income  
    0          2174             0              40  United-States  <=50K  
    1             0             0              13  United-States  <=50K  
    2             0             0              40  United-States  <=50K  
    3             0             0              40  United-States  <=50K  
    4             0             0              40           Cuba  <=50K  
    


```python
import pandas as pd

```


```python
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

```


```python
columns = [
    "age", "workclass", "fnlwgt", "education", "education-num", "marital-status",
    "occupation", "relationship", "race", "sex", "capital-gain", "capital-loss",
    "hours-per-week", "native-country", "income"
]

```


```python
census = pd.read_csv(url, names=columns, na_values=" ?", skipinitialspace=True)

```


```python
census.head()
census['income'].unique()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>workclass</th>
      <th>fnlwgt</th>
      <th>education</th>
      <th>education-num</th>
      <th>marital-status</th>
      <th>occupation</th>
      <th>relationship</th>
      <th>race</th>
      <th>sex</th>
      <th>capital-gain</th>
      <th>capital-loss</th>
      <th>hours-per-week</th>
      <th>native-country</th>
      <th>income</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>39</td>
      <td>State-gov</td>
      <td>77516</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Never-married</td>
      <td>Adm-clerical</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Male</td>
      <td>2174</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>1</th>
      <td>50</td>
      <td>Self-emp-not-inc</td>
      <td>83311</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Exec-managerial</td>
      <td>Husband</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>13</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>2</th>
      <td>38</td>
      <td>Private</td>
      <td>215646</td>
      <td>HS-grad</td>
      <td>9</td>
      <td>Divorced</td>
      <td>Handlers-cleaners</td>
      <td>Not-in-family</td>
      <td>White</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>3</th>
      <td>53</td>
      <td>Private</td>
      <td>234721</td>
      <td>11th</td>
      <td>7</td>
      <td>Married-civ-spouse</td>
      <td>Handlers-cleaners</td>
      <td>Husband</td>
      <td>Black</td>
      <td>Male</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>United-States</td>
      <td>&lt;=50K</td>
    </tr>
    <tr>
      <th>4</th>
      <td>28</td>
      <td>Private</td>
      <td>338409</td>
      <td>Bachelors</td>
      <td>13</td>
      <td>Married-civ-spouse</td>
      <td>Prof-specialty</td>
      <td>Wife</td>
      <td>Black</td>
      <td>Female</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>Cuba</td>
      <td>&lt;=50K</td>
    </tr>
  </tbody>
</table>
</div>




```python
census['income'].unique()
```




    array(['<=50K', '>50K'], dtype=object)




```python
# Fix the income bracket
def label_fix(label):
    label = label.strip().lower()
    if(label == '<=50k'):
        return 0
    return 1

```


```python
census['income'] = census['income'].apply(label_fix)

```


```python
census.rename(columns={"income": "income_bracket"}, inplace=True)

```


```python
census['income_bracket'].unique()

```




    array([0, 1])




```python
# Train Test Split
from sklearn.model_selection import train_test_split
```


```python
x_data = census.drop('income_bracket', axis=1)
y_labels = census['income_bracket']

X_train, x_test, y_train, y_est = train_test_split(x_data, y_labels, test_size=0.3, random_state=101)
```


```python
census.columns
```




    Index(['age', 'workclass', 'fnlwgt', 'education', 'education-num',
           'marital-status', 'occupation', 'relationship', 'race', 'sex',
           'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
           'income_bracket'],
          dtype='object')




```python
import tensorflow as tf
from tensorflow.feature_column import categorical_column_with_vocabulary_list as vlist
```


```python
from tensorflow.keras.layers import StringLookup
gender_lookup = StringLookup(vocabulary=["Female", "Male"], output_mode="int")
```


```python
gender
```




    VocabularyListCategoricalColumn(key='gender', vocabulary_list=('Female', 'Male'), dtype=tf.string, default_value=-1, num_oov_buckets=0)




```python
from tensorflow.feature_column import categorical_column_with_hash_bucket as bucket
```


```python
occupation = bucket("occupation", hash_bucket_size=1000)
marital_status = bucket("marital_status", hash_bucket_size=1000)
relationship = bucket("relationship", hash_bucket_size=1000)
education = bucket("education", hash_bucket_size=1000)
workclass = bucket("workclass", hash_bucket_size=1000)
native_country = bucket("native_country", hash_bucket_size=1000)
```


```python
from tensorflow.feature_column import numeric_column as nc
```


```python
age = nc("age")
education_num = nc("education_num")
capital_gain = nc("capital_gain")
capital_loss = nc("capital_loss")
hours_per_week = nc("hours_per_week")
```


```python
feat_cols = [gender, occupation, marital_status, relationship, education, workclass, native_country, age, education_num, 
            capital_gain, capital_loss, hours_per_week]
```


```python
feat_cols
```




    [VocabularyListCategoricalColumn(key='gender', vocabulary_list=('Female', 'Male'), dtype=tf.string, default_value=-1, num_oov_buckets=0),
     HashedCategoricalColumn(key='occupation', hash_bucket_size=1000, dtype=tf.string),
     HashedCategoricalColumn(key='marital_status', hash_bucket_size=1000, dtype=tf.string),
     HashedCategoricalColumn(key='relationship', hash_bucket_size=1000, dtype=tf.string),
     HashedCategoricalColumn(key='education', hash_bucket_size=1000, dtype=tf.string),
     HashedCategoricalColumn(key='workclass', hash_bucket_size=1000, dtype=tf.string),
     HashedCategoricalColumn(key='native_country', hash_bucket_size=1000, dtype=tf.string),
     NumericColumn(key='age', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None),
     NumericColumn(key='education_num', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None),
     NumericColumn(key='capital_gain', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None),
     NumericColumn(key='capital_loss', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None),
     NumericColumn(key='hours_per_week', shape=(1,), default_value=None, dtype=tf.float32, normalizer_fn=None)]




```python

```


---
**Score: 20**