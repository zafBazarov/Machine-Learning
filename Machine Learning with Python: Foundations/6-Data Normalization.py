
### Topic: Data Normalization. 
# - ensures that values share a common property.
# - often involves scaling data to fall within a small or specified range
# - is often required, reduces complexity and improves interpretability

# Data Normalization types
# - Z-Score Normalization: Transforms the data so that it has a mean of 0 and standard deviation of 1.
#        It often works well but some ML algorthim require lower and upper limits.

# - Min-Max Normalization: Transform the data from measured units to a new interval, which goes from lower to upper for feature F.
        # Both methods are suitable for a dataset whithout outliers.
# You can find the formulas for these methods on the internet.

#  - Log Transformation: Transform the data by replacing the values of the original data with its logarithm.
#       #  It works only with positive values. It is a good solution for outliers.

########################################################################
# How to Normalize data in Python

# Data preparation is to transform our data in order to make it more suitable for machine learning. 
    # During this step, we often have to restructure some of our data so that it conforms to a particular charachteristic. 
    # This is known as Normalization or Standardization. 
    # There are several ways to normalize data in python.

#########################################################
# How to perform min-max Normalization

# import packages
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import sklearn

# Import dataset
vehicles = pd.read_csv('vehicles.csv')
print(vehicles.head())
print(vehicles.info)

print(vehicles[['co2emissions']].describe())

# make a histogram 
vehicles[['co2emissions']].plot(kind = 'hist',
                                    bins = 20, 
                                    figsize = (10,6)
)
plt.show()

import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import matplotlib as mpl

vehicles = pd.read_csv('vehicles.csv')
from sklearn.preprocessing import MinMaxScaler
co2emissions_mm = MinMaxScaler().fit_transform(vehicles[['co2emissions']])
print(co2emissions_mm)

# create a data frame
co2emissions_mm = pd.DataFrame(co2emissions_mm, columns = ['co2emissions'])
print(co2emissions_mm)

print(co2emissions_mm.describe())
co2emissions_mm.plot(kind = 'hist',
                                    bins = 20, 
                                    figsize = (10,6)
)
plt.show()

###########################################################
## How to perform z-score Normalization
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import matplotlib as mpl

from sklearn.preprocessing import StandardScaler

vehicles = pd.read_csv('vehicles.csv')
co2emissions_zm = StandardScaler().fit_transform(vehicles[['co2emissions']])
co2emissions_zm = pd.DataFrame(co2emissions_zm, columns= ['co2emissions'])
print(co2emissions_zm.describe())

# visualise the data
co2emissions_zm.plot(kind = 'hist',
                                    bins = 20, 
                                    figsize = (10,6)
)
plt.show()

## How to perform log Normalization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

vehicles = pd.read_csv('vehicles.csv')

# np.log1p: This function computes the natural logarithm of (1 + x), which means it can handle zero 
# values without resulting in -inf. This is particularly useful if your data contains zeros.
co2emissions_log = np.log1p(vehicles['co2emissions'])

co2emissions_log = pd.DataFrame(co2emissions_log, columns= ['co2emissions'])
print(co2emissions_log.describe())

# visualise the data
co2emissions_log.plot(kind = 'hist',
                                    bins = 20, 
                                    figsize = (10,6)
)
plt.show()

# Add the log transformation as a new column to the dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

vehicles = pd.read_csv('vehicles.csv')

vehicles['co2emissions_log'] = np.log1p(vehicles['co2emissions'])
print(vehicles)

# visualise the data
vehicles['co2emissions_log'].plot(kind = 'hist',
                                    bins = 20, 
                                    figsize = (10,6)
)
plt.show()
