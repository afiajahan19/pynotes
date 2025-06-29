---
title: Json-To-Xml
date: 2025-06-29
author: Your Name
cell_count: 6
score: 5
---

```python
import xmltodict
```


```python
content = {
  "note" : {
    "to" : "Tove",
    "from" : "Jani",
    "heading" : "Reminder",
    "body" : "Don't forget me this weekend!"
  }
}
```


```python
content
```




    {'note': {'to': 'Tove',
      'from': 'Jani',
      'heading': 'Reminder',
      'body': "Don't forget me this weekend!"}}




```python
xml = xmltodict.unparse(content, pretty=True)
```


```python
xml
```




    '<?xml version="1.0" encoding="utf-8"?>\n<note>\n\t<to>Tove</to>\n\t<from>Jani</from>\n\t<heading>Reminder</heading>\n\t<body>Don\'t forget me this weekend!</body>\n</note>'




```python

```


---
**Score: 5**