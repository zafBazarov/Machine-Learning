
# Topic: Sampling 

    # This is the process of selecting a subset of the instances in a dataset as a proxy for the whole.

    # The original dataset is referred to as the population while the subset is known as a sample.
        # Sampling types: 
            # - random sampling without replacement
            # - random sampling with replacement
            # - stratified random sampling

##########################
# How to Sample Data in Python

# In order to get unbiased assessment of the performance of a supervised machine learning model,
# we need to evaluate it based on data that it di not previously ecnounter during the training process.
# To accomplish this, we must first split our data into a trining subset and a test subset prior to the model
# build stage. One common way to split data in this fashion is by creating non-overlapping subsets of the originial
# data using one of several sampling approaches.

# import dataset
import pandas as pd
vehicles = pd.read_csv("vehicles.csv")
print(vehicles)

# dependent variable
response = 'co2emissions'
y = vehicles[[response]]    
print(y.head())


# see dataset column names
predictors = list(vehicles.columns)
print(predictors)

# remove co2emissions form dataset 
predictors.remove(response)
print(predictors)

# independent variables

x = vehicles[predictors]
print(x.head())

################################################
## How to split data using Simple Random Sampling

import sklearn
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y)

# sample size
print(x_train.shape   )
print(y_train.shape   )

# random samle

print(x_test.shape   )
print(y_test.shape   )

# we can decide which percentage should be taken for random sampling
#40%

x_train, x_test, y_train, y_test = train_test_split(x,y, 
                                                    test_size= 0.4)
print(x_test.shape)

#############################################################################
## How to split data using Stratified Random Sampling


x_train, x_test, y_train, y_test = train_test_split(x,y, 
                                                    test_size= 0.01,
                                                    random_state= 1234 )
# we can see the distribution for the drive column
print (x['drive'].value_counts(normalize= True))

print (x_test['drive'].value_counts(normalize= True))

# split data using stratified random sampling method
x_train, x_test, y_train, y_test = train_test_split(x,y, 
                                                    test_size= 0.01,
                                                    random_state= 1234,
                                                     stratify=x['drive'] )
print (x_test['drive'].value_counts(normalize= True))
