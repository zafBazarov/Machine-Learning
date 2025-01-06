
## Data Cleaning

# Types of errors
# 1) **Missing vlues**. One of the most common errors is missing values. For example, if you have our shopping cart data, when you look closely, you can see that on the third line, the amount is missing. 
# 2) **Bad values**. Another type of errors are bad values. For example, in this shopping cart data, you can see that $217 for three pounds of carrot is a bit extreme. 
# 3) **Duplicated data**. And the last type I'm going to mention is duplicated data. If you look at this data, you will see that line number three and number five are duplicated. 

# These three kinds of errors are the ones I find most in data sets, and we'll cover how to detect and how to fix them.

# Missing values

# Let's explore the data. we hav cart.csv file. 

# library
import pandas as pd

# import data
df = pd.read_csv('cart.csv', parse_dates = ['date']
df


# Let's have a look at shopping cart data. Here is the data in a CSV format. We have the date, the name, the amount and the price. 
#So we import pandas as pd. And then we load the data frame and read in the data. 
# We see several missing values. Here we see NaN, not a number, and here we see NaN again. In the date column, we see NaT, not a time. 
# Pandas is trying to use the right missing value per type. Pandas also treat Python's none as a missing value. 
                 
# If you look at the amount column, you will see that it is a float. You can do it also by writing data frame.dtypes and hit Enter. And you see that the amount is float64. The problem is that integers do not have missing values. So pandas will convert integers to floating points in order to accommodate missing values. 
# Panda also have an IntegerArray type, which you can have integers with missing values. 

df['float'].astype('Int32')

#Let's do df amount astype Int32. And if you're going to run this cell, you're going to see now we get integer and another missing value, NA. How can you programmatically find out where are these missing values? You can use the pandas.isnull function or the isnull method of the data frame. So if I'm going to run data frame isnull, I'm going to get a data frame with true and false per cell but this is usually not what we want. 
df.isnull()

# In my case, I want to find out rows that have a missing value. So I'm going to do isnull and then ask any, so any of the value in the row in the first axis, the rows. If I'm going to run this cell, I'm going to see the rows that have missing values in them. 
df.isnull().any(axis=1)
# Note that the empty string is not considered a missing value. You will need to use Boolean indexing to find this.
