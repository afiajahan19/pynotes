---
title: Runnable-Lambda
date: 2025-06-27
author: Your Name
cell_count: 6
score: 5
---

```python
!pip install langchain langchain-openai

```

    Collecting langchain
      Downloading langchain-0.3.26-py3-none-any.whl.metadata (7.8 kB)
    Collecting langchain-openai
      Downloading langchain_openai-0.3.26-py3-none-any.whl.metadata (2.3 kB)
    Collecting langchain-core<1.0.0,>=0.3.66 (from langchain)
      Downloading langchain_core-0.3.66-py3-none-any.whl.metadata (5.8 kB)
    Collecting langchain-text-splitters<1.0.0,>=0.3.8 (from langchain)
      Downloading langchain_text_splitters-0.3.8-py3-none-any.whl.metadata (1.9 kB)
    Collecting langsmith>=0.1.17 (from langchain)
      Downloading langsmith-0.4.3-py3-none-any.whl.metadata (15 kB)
    Collecting pydantic<3.0.0,>=2.7.4 (from langchain)
      Downloading pydantic-2.11.7-py3-none-any.whl.metadata (67 kB)
    Collecting SQLAlchemy<3,>=1.4 (from langchain)
      Downloading sqlalchemy-2.0.41-cp312-cp312-win_amd64.whl.metadata (9.8 kB)
    Requirement already satisfied: requests<3,>=2 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from langchain) (2.32.4)
    Requirement already satisfied: PyYAML>=5.3 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from langchain) (6.0.2)
    Collecting tenacity!=8.4.0,<10.0.0,>=8.1.0 (from langchain-core<1.0.0,>=0.3.66->langchain)
      Downloading tenacity-9.1.2-py3-none-any.whl.metadata (1.2 kB)
    Collecting jsonpatch<2.0,>=1.33 (from langchain-core<1.0.0,>=0.3.66->langchain)
      Downloading jsonpatch-1.33-py2.py3-none-any.whl.metadata (3.0 kB)
    Collecting packaging<25,>=23.2 (from langchain-core<1.0.0,>=0.3.66->langchain)
      Downloading packaging-24.2-py3-none-any.whl.metadata (3.2 kB)
    Requirement already satisfied: typing-extensions>=4.7 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from langchain-core<1.0.0,>=0.3.66->langchain) (4.14.0)
    Requirement already satisfied: jsonpointer>=1.9 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from jsonpatch<2.0,>=1.33->langchain-core<1.0.0,>=0.3.66->langchain) (3.0.0)
    Collecting annotated-types>=0.6.0 (from pydantic<3.0.0,>=2.7.4->langchain)
      Downloading annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
    Collecting pydantic-core==2.33.2 (from pydantic<3.0.0,>=2.7.4->langchain)
      Downloading pydantic_core-2.33.2-cp312-cp312-win_amd64.whl.metadata (6.9 kB)
    Collecting typing-inspection>=0.4.0 (from pydantic<3.0.0,>=2.7.4->langchain)
      Downloading typing_inspection-0.4.1-py3-none-any.whl.metadata (2.6 kB)
    Requirement already satisfied: charset_normalizer<4,>=2 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from requests<3,>=2->langchain) (3.4.2)
    Requirement already satisfied: idna<4,>=2.5 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from requests<3,>=2->langchain) (3.10)
    Requirement already satisfied: urllib3<3,>=1.21.1 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from requests<3,>=2->langchain) (2.5.0)
    Requirement already satisfied: certifi>=2017.4.17 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from requests<3,>=2->langchain) (2025.6.15)
    Collecting greenlet>=1 (from SQLAlchemy<3,>=1.4->langchain)
      Downloading greenlet-3.2.3-cp312-cp312-win_amd64.whl.metadata (4.2 kB)
    Collecting openai<2.0.0,>=1.86.0 (from langchain-openai)
      Downloading openai-1.92.2-py3-none-any.whl.metadata (29 kB)
    Collecting tiktoken<1,>=0.7 (from langchain-openai)
      Downloading tiktoken-0.9.0-cp312-cp312-win_amd64.whl.metadata (6.8 kB)
    Requirement already satisfied: anyio<5,>=3.5.0 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from openai<2.0.0,>=1.86.0->langchain-openai) (4.9.0)
    Collecting distro<2,>=1.7.0 (from openai<2.0.0,>=1.86.0->langchain-openai)
      Downloading distro-1.9.0-py3-none-any.whl.metadata (6.8 kB)
    Requirement already satisfied: httpx<1,>=0.23.0 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from openai<2.0.0,>=1.86.0->langchain-openai) (0.28.1)
    Collecting jiter<1,>=0.4.0 (from openai<2.0.0,>=1.86.0->langchain-openai)
      Downloading jiter-0.10.0-cp312-cp312-win_amd64.whl.metadata (5.3 kB)
    Requirement already satisfied: sniffio in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from openai<2.0.0,>=1.86.0->langchain-openai) (1.3.1)
    Collecting tqdm>4 (from openai<2.0.0,>=1.86.0->langchain-openai)
      Downloading tqdm-4.67.1-py3-none-any.whl.metadata (57 kB)
    Requirement already satisfied: httpcore==1.* in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from httpx<1,>=0.23.0->openai<2.0.0,>=1.86.0->langchain-openai) (1.0.9)
    Requirement already satisfied: h11>=0.16 in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from httpcore==1.*->httpx<1,>=0.23.0->openai<2.0.0,>=1.86.0->langchain-openai) (0.16.0)
    Collecting regex>=2022.1.18 (from tiktoken<1,>=0.7->langchain-openai)
      Downloading regex-2024.11.6-cp312-cp312-win_amd64.whl.metadata (41 kB)
    Collecting orjson<4.0.0,>=3.9.14 (from langsmith>=0.1.17->langchain)
      Downloading orjson-3.10.18-cp312-cp312-win_amd64.whl.metadata (43 kB)
    Collecting requests-toolbelt<2.0.0,>=1.0.0 (from langsmith>=0.1.17->langchain)
      Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl.metadata (14 kB)
    Collecting zstandard<0.24.0,>=0.23.0 (from langsmith>=0.1.17->langchain)
      Downloading zstandard-0.23.0-cp312-cp312-win_amd64.whl.metadata (3.0 kB)
    Requirement already satisfied: colorama in c:\users\afia jahan\anaconda3\envs\py312\lib\site-packages (from tqdm>4->openai<2.0.0,>=1.86.0->langchain-openai) (0.4.6)
    Downloading langchain-0.3.26-py3-none-any.whl (1.0 MB)
       ---------------------------------------- 0.0/1.0 MB ? eta -:--:--
       ---------------------------------------- 1.0/1.0 MB 9.6 MB/s eta 0:00:00
    Downloading langchain_core-0.3.66-py3-none-any.whl (438 kB)
    Downloading jsonpatch-1.33-py2.py3-none-any.whl (12 kB)
    Downloading langchain_text_splitters-0.3.8-py3-none-any.whl (32 kB)
    Downloading packaging-24.2-py3-none-any.whl (65 kB)
    Downloading pydantic-2.11.7-py3-none-any.whl (444 kB)
    Downloading pydantic_core-2.33.2-cp312-cp312-win_amd64.whl (2.0 MB)
       ---------------------------------------- 0.0/2.0 MB ? eta -:--:--
       ---------------------------------------- 2.0/2.0 MB 21.7 MB/s eta 0:00:00
    Downloading sqlalchemy-2.0.41-cp312-cp312-win_amd64.whl (2.1 MB)
       ---------------------------------------- 0.0/2.1 MB ? eta -:--:--
       ---------------------------------------- 2.1/2.1 MB 17.0 MB/s eta 0:00:00
    Downloading tenacity-9.1.2-py3-none-any.whl (28 kB)
    Downloading langchain_openai-0.3.26-py3-none-any.whl (70 kB)
    Downloading openai-1.92.2-py3-none-any.whl (753 kB)
       ---------------------------------------- 0.0/753.3 kB ? eta -:--:--
       --------------------------------------- 753.3/753.3 kB 32.7 MB/s eta 0:00:00
    Downloading distro-1.9.0-py3-none-any.whl (20 kB)
    Downloading jiter-0.10.0-cp312-cp312-win_amd64.whl (206 kB)
    Downloading tiktoken-0.9.0-cp312-cp312-win_amd64.whl (894 kB)
       ---------------------------------------- 0.0/894.9 kB ? eta -:--:--
       ---------------------- ---------------- 524.3/894.9 kB 16.4 MB/s eta 0:00:01
       ----------------------------------- ---- 786.4/894.9 kB 1.4 MB/s eta 0:00:01
       ---------------------------------------- 894.9/894.9 kB 1.2 MB/s eta 0:00:00
    Downloading annotated_types-0.7.0-py3-none-any.whl (13 kB)
    Downloading greenlet-3.2.3-cp312-cp312-win_amd64.whl (297 kB)
    Downloading langsmith-0.4.3-py3-none-any.whl (367 kB)
    Downloading orjson-3.10.18-cp312-cp312-win_amd64.whl (134 kB)
    Downloading requests_toolbelt-1.0.0-py2.py3-none-any.whl (54 kB)
    Downloading zstandard-0.23.0-cp312-cp312-win_amd64.whl (495 kB)
    Downloading regex-2024.11.6-cp312-cp312-win_amd64.whl (273 kB)
    Downloading tqdm-4.67.1-py3-none-any.whl (78 kB)
    Downloading typing_inspection-0.4.1-py3-none-any.whl (14 kB)
    Installing collected packages: zstandard, typing-inspection, tqdm, tenacity, regex, pydantic-core, packaging, orjson, jsonpatch, jiter, greenlet, distro, annotated-types, tiktoken, SQLAlchemy, requests-toolbelt, pydantic, openai, langsmith, langchain-core, langchain-text-splitters, langchain-openai, langchain
    
       - --------------------------------------  1/23 [typing-inspection]
       --- ------------------------------------  2/23 [tqdm]
       --- ------------------------------------  2/23 [tqdm]
       ----- ----------------------------------  3/23 [tenacity]
       ------ ---------------------------------  4/23 [regex]
       ------ ---------------------------------  4/23 [regex]
       -------- -------------------------------  5/23 [pydantic-core]
      Attempting uninstall: packaging
       -------- -------------------------------  5/23 [pydantic-core]
        Found existing installation: packaging 25.0
       -------- -------------------------------  5/23 [pydantic-core]
        Uninstalling packaging-25.0:
       -------- -------------------------------  5/23 [pydantic-core]
          Successfully uninstalled packaging-25.0
       -------- -------------------------------  5/23 [pydantic-core]
       ---------- -----------------------------  6/23 [packaging]
       ---------- -----------------------------  6/23 [packaging]
       ------------ ---------------------------  7/23 [orjson]
       --------------- ------------------------  9/23 [jiter]
       ----------------- ---------------------- 10/23 [greenlet]
       ----------------- ---------------------- 10/23 [greenlet]
       ----------------- ---------------------- 10/23 [greenlet]
       -------------------- ------------------- 12/23 [annotated-types]
       ---------------------- ----------------- 13/23 [tiktoken]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       ------------------------ --------------- 14/23 [SQLAlchemy]
       -------------------------- ------------- 15/23 [requests-toolbelt]
       -------------------------- ------------- 15/23 [requests-toolbelt]
       -------------------------- ------------- 15/23 [requests-toolbelt]
       --------------------------- ------------ 16/23 [pydantic]
       --------------------------- ------------ 16/23 [pydantic]
       --------------------------- ------------ 16/23 [pydantic]
       --------------------------- ------------ 16/23 [pydantic]
       --------------------------- ------------ 16/23 [pydantic]
       --------------------------- ------------ 16/23 [pydantic]
       --------------------------- ------------ 16/23 [pydantic]
       --------------------------- ------------ 16/23 [pydantic]
       --------------------------- ------------ 16/23 [pydantic]
       --------------------------- ------------ 16/23 [pydantic]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ----------------------------- ---------- 17/23 [openai]
       ------------------------------- -------- 18/23 [langsmith]
       ------------------------------- -------- 18/23 [langsmith]
       ------------------------------- -------- 18/23 [langsmith]
       ------------------------------- -------- 18/23 [langsmith]
       ------------------------------- -------- 18/23 [langsmith]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       --------------------------------- ------ 19/23 [langchain-core]
       ---------------------------------- ----- 20/23 [langchain-text-splitters]
       ---------------------------------- ----- 20/23 [langchain-text-splitters]
       ------------------------------------ --- 21/23 [langchain-openai]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       -------------------------------------- - 22/23 [langchain]
       ---------------------------------------- 23/23 [langchain]
    
    Successfully installed SQLAlchemy-2.0.41 annotated-types-0.7.0 distro-1.9.0 greenlet-3.2.3 jiter-0.10.0 jsonpatch-1.33 langchain-0.3.26 langchain-core-0.3.66 langchain-openai-0.3.26 langchain-text-splitters-0.3.8 langsmith-0.4.3 openai-1.92.2 orjson-3.10.18 packaging-24.2 pydantic-2.11.7 pydantic-core-2.33.2 regex-2024.11.6 requests-toolbelt-1.0.0 tenacity-9.1.2 tiktoken-0.9.0 tqdm-4.67.1 typing-inspection-0.4.1 zstandard-0.23.0
    


```python
from constants import OPENAI_API_KEY
import os
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
```


```python
from langchain_openai import ChatOpenAI
from langchain_core.runnables import chain
```


```python
tech_dict = {
    "py": "python",
    "ja": "java"
}

@chain
async def expand_word(word: str):
    if word in tech_dict:
        return tech_dict[word]
    return "unknown"

@chain
async def fill_info(word: str):
    expanded_word = await expand_word.ainvoke(word)
    return expanded_word.title()

```


```python
import nest_asyncio
import asyncio
nest_asyncio.apply()

# Run the async chain
result = await fill_info.ainvoke("py")
print(result)  # Output: Python

```

    Python
    


```python

```


---
**Score: 5**