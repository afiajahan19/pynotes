---
title: Seabornflightdataanalysis
date: 2025-06-28
author: Your Name
cell_count: 9
score: 5
---

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

```


```python
flights = sns.load_dataset("flights")
flights.head()


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
      <th>year</th>
      <th>month</th>
      <th>passengers</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1949</td>
      <td>Jan</td>
      <td>112</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1949</td>
      <td>Feb</td>
      <td>118</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1949</td>
      <td>Mar</td>
      <td>132</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1949</td>
      <td>Apr</td>
      <td>129</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1949</td>
      <td>May</td>
      <td>121</td>
    </tr>
  </tbody>
</table>
</div>




```python
flights_wide = flights.pivot(index="year", columns="month", values="passengers")
flights_wide.head()

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
      <th>month</th>
      <th>Jan</th>
      <th>Feb</th>
      <th>Mar</th>
      <th>Apr</th>
      <th>May</th>
      <th>Jun</th>
      <th>Jul</th>
      <th>Aug</th>
      <th>Sep</th>
      <th>Oct</th>
      <th>Nov</th>
      <th>Dec</th>
    </tr>
    <tr>
      <th>year</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1949</th>
      <td>112</td>
      <td>118</td>
      <td>132</td>
      <td>129</td>
      <td>121</td>
      <td>135</td>
      <td>148</td>
      <td>148</td>
      <td>136</td>
      <td>119</td>
      <td>104</td>
      <td>118</td>
    </tr>
    <tr>
      <th>1950</th>
      <td>115</td>
      <td>126</td>
      <td>141</td>
      <td>135</td>
      <td>125</td>
      <td>149</td>
      <td>170</td>
      <td>170</td>
      <td>158</td>
      <td>133</td>
      <td>114</td>
      <td>140</td>
    </tr>
    <tr>
      <th>1951</th>
      <td>145</td>
      <td>150</td>
      <td>178</td>
      <td>163</td>
      <td>172</td>
      <td>178</td>
      <td>199</td>
      <td>199</td>
      <td>184</td>
      <td>162</td>
      <td>146</td>
      <td>166</td>
    </tr>
    <tr>
      <th>1952</th>
      <td>171</td>
      <td>180</td>
      <td>193</td>
      <td>181</td>
      <td>183</td>
      <td>218</td>
      <td>230</td>
      <td>242</td>
      <td>209</td>
      <td>191</td>
      <td>172</td>
      <td>194</td>
    </tr>
    <tr>
      <th>1953</th>
      <td>196</td>
      <td>196</td>
      <td>236</td>
      <td>235</td>
      <td>229</td>
      <td>243</td>
      <td>264</td>
      <td>272</td>
      <td>237</td>
      <td>211</td>
      <td>180</td>
      <td>201</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.lineplot(data=flights_wide["May"])
plt.title("May Passengers (1949–1960)")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.show()

```


    
![png](/pynotes/images/seabornflightdataanalysis_3_0.png)
    



```python
sns.lineplot(data=flights_wide["Oct"])
plt.title("October Passengers (1949–1960)")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.show()

```


    
![png](/pynotes/images/seabornflightdataanalysis_4_0.png)
    



```python
sns.lineplot(data=flights_wide)
plt.title("Monthly Passenger Trends (1949–1960)")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.show()

```


    
![png](/pynotes/images/seabornflightdataanalysis_5_0.png)
    



```python
data = {
    'month': [0, 1, 2],
    'raja': [0, 300, 450],
    'hari': [0, 200, 500]
}
df = pd.DataFrame(data)
sns.lineplot(data=df.drop(columns='month'))
plt.title("Scores Over Time (Raja vs Hari)")
plt.show()

```


    
![png](/pynotes/images/seabornflightdataanalysis_6_0.png)
    



```python
data = {
    'days': [1, 1, 1, 2, 2, 2],
    'learners': ['raja', 'hari', 'steve', 'raja', 'hari', 'steve'],
    'score': [0, 0, 0, 50, 40, 60]
}
df = pd.DataFrame(data)
df_wide = df.pivot(index="days", columns="learners", values="score")
sns.lineplot(data=df_wide)
plt.title("Learner Scores Over Days")
plt.xlabel("Day")
plt.ylabel("Score")
plt.show()

```


    
![png](/pynotes/images/seabornflightdataanalysis_7_0.png)
    



```python

```


---
**Score: 5**