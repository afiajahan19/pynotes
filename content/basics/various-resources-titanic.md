---
title: Various-Resources-Titanic
date: 2025-06-27
author: Your Name
cell_count: 2
score: 0
---

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load working dataset
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# Select needed columns
data = df[['Survived', 'Sex', 'Age']]

# Fill missing Age values with mean
data.loc[:, 'Age'] = data['Age'].fillna(data['Age'].mean())


# Convert 'Sex' to dummy variables
data = pd.get_dummies(data, columns=['Sex'])

# Define features and target
X = data.drop('Survived', axis=1)
y = data['Survived']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21)

# Define models
models = [
    KNeighborsClassifier(),
    LogisticRegression(solver="liblinear"),
    SVC(kernel="linear"),
    GaussianNB(),
    MLPClassifier(max_iter=500),
    DecisionTreeClassifier(),
    RandomForestClassifier()
]

# Evaluate models
for model in models:
    name = model.__class__.__name__
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print("-" * 30)
    print(f"{name}:\nAccuracy: {acc:.4%}")

```

    ------------------------------
    KNeighborsClassifier:
    Accuracy: 76.4925%
    ------------------------------
    LogisticRegression:
    Accuracy: 78.7313%
    ------------------------------
    SVC:
    Accuracy: 78.7313%
    ------------------------------
    GaussianNB:
    Accuracy: 78.7313%
    ------------------------------
    MLPClassifier:
    Accuracy: 79.1045%
    ------------------------------
    DecisionTreeClassifier:
    Accuracy: 77.6119%
    ------------------------------
    RandomForestClassifier:
    Accuracy: 79.1045%
    


```python

```


---
**Score: 0**