
### How to Visualize Data in Python

# Import data
import pandas as pd
vehicles = pd.read_csv('vehicles.csv')
vehicles.head()

# Create a relationship visualization
# Scatterplot

vehicles.plot(kind = 'scatter', x='citympg', y='co2emissions')

# Create a distribution visualization
# Histogram
vehicles['co2emissions'].plot(kind='hist')

## Create a comparison visualiyation
# Pivot table
vehicles.pivot(columns='drive', values='co2emissions')

# Boxplot
vehicles.pivot(columns='drive', values='co2emissions').plot(kind='box',
                                                    figsize = (10,6))

## Create a composition visualization

vehicles.groupby('year')['drive'].value_counts()

vehicles.groupby('year')['drive'].value_counts().unstack()

vehicles.groupby('year')['drive'].value_counts().unstack().plot(kind ='bar',
                                                    stacked= True, 
                                                    figsize = (10,6) )

