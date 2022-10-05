# Data Preprocessing

prepare data, so the ML model will not go wrong.

## Get Dataset

[Super Data Science](https://www.superdatascience.com/pages/machine-learning)

**Use independent variables to predict dependent variable.**

## Import Library

Python

```py
import numpy as np # mathematical S
import matplotlib.pyplot as plt # for plot
import pandas as pd # import and manage datasets
```

R

most essential library is imported by default

## Import Dataset

! set working directory

Python

```py
dataset = pd.read_csv("Data.csv")
```

R

```r
dataset = read.csv("Data.csv")
```

## Missing Data

1. remove the row of missing data (DANGEROUS)
2. replace the missing data with the mean of column (Recommended)
   - or medium or most_frequent of a constant value



## Categorical Data

- like yes or no, male or female
- can be represented as numbers

Because numbers have sequence, the ML model may judge the values transformed.

To prevent this, multiple columns will be used.

```
Country     France   Spain  German
Spain       0        1      0
German      0        0      1
Spain       0        1      0
France  =>  1        0      0
Spain       0        1      0
German      0        0      1
France      1        0      0
```

