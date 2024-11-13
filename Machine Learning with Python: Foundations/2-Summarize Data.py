
#### How  to Summarize Data in Python

## import pandas library and data
import pandas as pd
washers = pd.read_csv("washers.csv")

## Describe a DataFrame

washers.info()

washers.head()

## Get Simple Aggregations
# The describe() method returns a statistical summary for each of the columns in a DataFrame. 
# The descriptive statistics returned by the describe() method depends on the data type of a clomun.

washers.describe()

washers['BrandName'].describe()

washers['Volume'].describe()


washers['BrandName'].value_counts()
washers['BrandName'].value_counts(normalize = True)


washers[['Volume']].mean()

### Group level Aggregation

washers.groupby('BrandName')[['Volume']].mean()

### Sort function

washers.groupby('BrandName')[['Volume']].mean().sort_values (by='Volume')

### Agg function

washers.groupby('BrandName')[['Volume']].agg(['mean', 'median', 'min', 'max', 'std'])


