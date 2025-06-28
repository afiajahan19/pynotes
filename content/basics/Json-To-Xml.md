---
title: Json-To-Xml
date: 2025-06-28
author: Your Name
cell_count: 4
score: 0
---

```python
!pip install xmltodict

```

    Collecting xmltodict
      Downloading xmltodict-0.14.2-py2.py3-none-any.whl.metadata (8.0 kB)
    Downloading xmltodict-0.14.2-py2.py3-none-any.whl (10.0 kB)
    Installing collected packages: xmltodict
    Successfully installed xmltodict-0.14.2
    

    WARNING: Ignoring invalid distribution ~umpy (C:\Users\Afia Jahan\anaconda3\envs\py312\Lib\site-packages)
    WARNING: Ignoring invalid distribution ~umpy (C:\Users\Afia Jahan\anaconda3\envs\py312\Lib\site-packages)
    WARNING: Ignoring invalid distribution ~umpy (C:\Users\Afia Jahan\anaconda3\envs\py312\Lib\site-packages)
    


```python
json_data = {
    "person": {
        "name": "Alice",
        "age": 30,
        "phones": ["123-4567", "987-6543"]
    }
}

```


```python
import xmltodict

# Convert JSON (Python dict) to XML
xml_output = xmltodict.unparse({"root": json_data}, pretty=True)
print(xml_output)


```

    <?xml version="1.0" encoding="utf-8"?>
    <root>
    	<person>
    		<name>Alice</name>
    		<age>30</age>
    		<phones>123-4567</phones>
    		<phones>987-6543</phones>
    	</person>
    </root>
    


```python

```


---
**Score: 0**