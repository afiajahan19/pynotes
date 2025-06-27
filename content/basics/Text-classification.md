---
title: Text-Classification
date: 2025-06-27
author: Your Name
cell_count: 4
score: 0
---

```python
import re
import pandas as pd
import numpy as np
from collections import defaultdict

# Step 1: Preprocessing function
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()

# Step 2: Naive Bayes training function
def train_naive_bayes(df, alpha=1.0):
    classes = df['label'].unique()
    cls_word_counts = {c: defaultdict(int) for c in classes}
    cls_doc_counts = df['label'].value_counts().to_dict()
    vocab = set()

    for _, row in df.iterrows():
        c = row['label']
        words = preprocess(row['text'])
        for w in words:
            cls_word_counts[c][w] += 1
            vocab.add(w)

    total_docs = len(df)
    cls_priors = {c: cls_doc_counts[c] / total_docs for c in classes}
    cls_word_totals = {c: sum(cls_word_counts[c].values()) for c in classes}

    def predict(text):
        words = preprocess(text)
        scores = {}
        V = len(vocab)
        for c in classes:
            log_prob = np.log(cls_priors[c])
            for w in words:
                count = cls_word_counts[c].get(w, 0)
                log_prob += np.log((count + alpha) / (cls_word_totals[c] + alpha * V))
            scores[c] = log_prob
        return max(scores, key=scores.get)

    return predict, vocab, cls_word_totals, cls_priors

# Step 3: Example dataset
df = pd.DataFrame({
    'text': [
        'I love this movie, it is fantastic!',
        'This film is terrible, I hate it.',
        'What a wonderful experience, great acting.',
        'Worst movie ever, so boring and awful.'
    ],
    'label': ['pos', 'neg', 'pos', 'neg']
})

# Step 4: Split into training and test data (3 train, 1 test)
train_df = df.iloc[:3]
test_df = df.iloc[3:]

# Step 5: Train the model
predict, vocab, cls_word_totals, cls_priors = train_naive_bayes(train_df)

# Step 6: Evaluate on test set
predictions = test_df['text'].apply(predict)
accuracy = (predictions == test_df['label']).mean()

# Step 7: Output
print(f"Accuracy: {accuracy:.2f}")
print("\nPredictions:")
print(test_df[['text', 'label']], '->', list(predictions))

# Step 8: Debug Info
print("\nVocab:", vocab)
print("Class Word Totals:", cls_word_totals)
print("Class Priors:", cls_priors)

# Step 9: Try on new unseen sentences
print("\nNew predictions:")
print("Sentence: 'Awful movie, I hated every second' ->", predict("Awful movie, I hated every second"))
print("Sentence: 'Beautiful acting and direction' ->", predict("Beautiful acting and direction"))

```

    Accuracy: 1.00
    
    Predictions:
                                         text label
    3  Worst movie ever, so boring and awful.   neg -> ['neg']
    
    Vocab: {'it', 'experience', 'terrible', 'acting', 'is', 'wonderful', 'movie', 'fantastic', 'film', 'a', 'hate', 'love', 'what', 'i', 'great', 'this'}
    Class Word Totals: {'pos': 13, 'neg': 7}
    Class Priors: {'pos': 0.6666666666666666, 'neg': 0.3333333333333333}
    
    New predictions:
    Sentence: 'Awful movie, I hated every second' -> neg
    Sentence: 'Beautiful acting and direction' -> pos
    


```python

```


```python

```


```python

```


---
**Score: 0**