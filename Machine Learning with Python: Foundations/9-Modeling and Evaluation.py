#####
# Topic: Modeling and Evaluation

    # Appply a machine learning approach to your data 
    # We have two problems in Supervised machine Learning
    #    - Classification promlem: Supervised machine learnig problem where the dependent varibale is categorical, color, gender and so on
    #    - Regression problem:  upervised machine learnig problem where the dependent varibale is categorcontinuousical, income, age ...
    # 
    # 
# Ealuation 
#   Assess how well your machine learning approach worked# 

###########################################################
## How to Build Machine Learning Model in Python

# In the modeling stage of the machine learning process, our goal is to choose and apply the appropriate machine learning approach that 
# works with the data we have and sloves the portion that we intend to solve. If our objective is to build a model
# that predicts a numeric or continuos value, then our problem is known as a regression problem. One of the most
# common models used in solving regression problems is Linear Regression#

# Collect the data

import pandas as pd
bikes = pd.read_csv('bikes.csv')
print(bikes.head())


# Explore the Data
print(bikes.info())

# summary statistics

print(bikes.describe())

# creating a scatter plot to identify relationship between temperature and rentals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

bikes.plot(kind = 'scatter', x='temperature', y='rentals')
plt.show()

bikes.plot(kind = 'scatter', x='humidity', y='rentals')
plt.show()

bikes.plot(kind = 'scatter', x='windspeed', y='rentals')
plt.show()

# Prepare the data

# dependent variable
response = 'rentals'
y = bikes[[response]]
print(y)

# independent variables

predictors = list(bikes.columns)
predictors.remove(response)
x = bikes[predictors]
print(x)

# split data to test and train samples
import sklearn
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state= 1234)

#### Train the Model

# Linear regression model
from sklearn.linear_model import LinearRegression

model = LinearRegression().fit(x_train, y_train)

print(model.intercept_)
print(model.coef_)

# The model coefficients correspond to the order in which the independent variables are listed in the 
# training data. Theis means that the equation for the fitted regression line can be writte as: 
# y = 3800.68 + 80,35*temperature - 4665,74*humidity - 196,22*windspeed
# 
# With the linear regression equation, we can estimate what our model will predict given any 
# weather condition. For example, given a temperature of 72 F, 22% humidity and windspeed 5 miles per hour, 
# our model would predict: 
# 7.578 bikes = 3800,68 + 80,35*72 - 4665,74*0.22 - 196,22*5# 

#######################
## Evaluate the Model

# R2 value shows this command. tells us that our model is able to explain 98.2% of the variablity in the response 
# values of the test data 
print(model.score(x_test, y_test))

# Accurate = absolute error function
# calculate mean absolute error between actual response values# 
y_pred = model.predict(x_test)

from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(y_test, y_pred))

# To be off mark by an average of plus or minus 194 bikes.