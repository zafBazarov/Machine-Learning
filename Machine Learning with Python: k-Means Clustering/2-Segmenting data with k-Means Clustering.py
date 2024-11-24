
#######
## Topic: Segmenting data with k-Means Clustering

# Learning Objectives:
# The primay objective of clsutering is to group items within a dataset based on similarity. 
# k-means Clustering is one of the most popular and easy to use clustering approaches. 
# With k-Means Clustering, similarity is based on a distance metric know as euclidian distance#

# 1) Import and Explore the Data

import pandas as pd
customers = pd.read_csv("mallcustomers.csv")

print(customers.head())

#### 2) Explore the Data

print(customers.info())

# summary statistics
print(customers.describe(include='all').round(2))

# visual exploration - boxplot

from matplotlib import pyplot as plt
import seaborn as sns
sns.set_theme()

# gender vs income
ax=sns.boxplot(data=customers,
               x='Gender',
               y='Income',
               palette = 'colorblind')
#plt.show()

# gender vs age
ax=sns.boxplot(data=customers,
               x='Gender',
               y='Age',
               palette = 'colorblind')
#plt.show()

# gender vs spending
ax=sns.boxplot(data=customers,
               x='Gender',
               y='SpendingScore',
               palette = 'colorblind')
#plt.show()


##### scatterplot

# income vs age
ax=sns.scatterplot(data=customers,
               x='Age',
               y='Income',
               s=150)
#plt.show()

# income vs spending
ax=sns.scatterplot(data=customers,
               x='Age',
               y='SpendingScore',
               s=150)
#plt.show()

# income vs spending
ax=sns.scatterplot(data=customers,
               x='Income',
               y='SpendingScore',
               s=150)
#plt.show()


# 2)Prepare the Data

# filter variables
print(customers[['Income', 'SpendingScore']].describe().round(2))

# import packages
import sklearn
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Z-score normalization

customers_scaled = scaler.fit_transform(customers[['Income', 'SpendingScore']])

customers_scaled = pd.DataFrame(customers_scaled, columns=['Income', 'Spending'])

print(customers_scaled.describe().round(2))

## 3) Create the Clusters

from sklearn.cluster import KMeans
km = KMeans(n_clusters= 3, n_init=25, random_state=1234)

km.fit(customers_scaled)

print (km.labels_)

print (km.inertia_)