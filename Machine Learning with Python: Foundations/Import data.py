import pandas as pd

### The pandas Series
members = ("Brazil", "Russia", "India", "China", "South Africa")

brics1 = pd.Series(members)

brics1

type(brics1)

#### Th pandas DataFrame

members2 = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
           "capital" :["Brailisa", "Moscow", "New Dehli", "Beijing", "Pretoria"],
           "gdp": [2750, 1658, 3202, 15270, 370],
           "literacy":[.944, .997, .721, .964, .943],
           "expectancy": [76.8, 72.7, 68.8, 76.4, 63.6],
           "population": [210.87, 143.96, 1367.09, 1415.05, 57.4]}
print(members2)

brics2 = pd.DataFrame(members2)
brics2

type(brics2)


### 2 data frame

members3 = (["Brazil", "Brailisa", 2750, 944, 76.8, 7210.87],
           ["Russia", "Moscow", 1658, .997, 72.7, 143.96],
           ["India", "New Dehli", 3202, .721, 68.8, 1367.09],
           ["China", "Beijing", 15270, .964, 76.4, 1415.05],
           ["South Africa","Pretoria", 370, .943, 63.6, 57.4])
labels = ["country", "capital", "gdp", "literacy", "literacy", "expectancy"]

brics3 = pd.DataFrame(members3, columns=labels)

brics3

## How to omport data from a CSV file

brics4= pd.read_csv("brics.csv")
brics4

## How to omport data from an Excel file

brics5 = pd.read_excel("brics.xlsx")
brics5

## To read the second sheet on excel file

brics6 = pd.read_excel("brics.xlsx", sheet_name="Summits")

