
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

customers_scaled = pd.DataFrame(customers_scaled, columns=['Income', 'SpendingScore'])

print(customers_scaled.describe().round(2))

## 3) Create the Clusters

from sklearn.cluster import KMeans
km = KMeans(n_clusters= 3, n_init=25, random_state=1234)

km.fit(customers_scaled)

print (km.labels_)

print (km.inertia_)

######################

# 4) Evaluate and Visualize the Clusters

# one of the method to identify a cluster quality is to look its size
# This query helps us for this purpose
print(pd.Series(km.labels_).value_counts().sort_index())

# these are clusters with customer numbers   0-38, 1-39, 2-123.
# 2 second cluster must be checked

# now check the cluster centroids
print(km.cluster_centers_)

cluster_centers = pd.DataFrame(km.cluster_centers_,
                               columns= ['Income', 'SpendingScore'])

print(cluster_centers)

# Another way to identify a cluster quality is jut to visualise them.
# Set the figure size 

plt.figure(figsize=(10,8))

# Plot the Cluster

ax = sns.scatterplot(data=customers_scaled,
                     x='Income',
                     y='SpendingScore',
                     hue= km.labels_,
                     palette='colorblind',
                     alpha=0.8,
                     s=150,
                     legend=False)

#plt.show()

# Plot the Centroids

ax = sns.scatterplot(data= cluster_centers,
                     x='Income',
                     y='SpendingScore',
                     hue= cluster_centers.index,
                     palette='colorblind',
                     s=600,
                     marker='D',
                     ec = 'black',
                     legend=False)

#plt.show()

# Add centroid labels

for i in range (len(cluster_centers)):
            plt.text(x = cluster_centers.Income[i],
                     y= cluster_centers.SpendingScore[i],
                     s=i,
                     horizontalalignment = 'center',
                     verticalalignment = 'center',
                     size = 15,
                     weight = 'bold',
                     color = 'white'
                                       )
#plt.show()


###################################

# 5) Choose the right number of Clusters

# The Within Cluster Sum of Squares (WCSS)

wcss = []
for k in range(2, 11):
    km = KMeans(n_clusters= k, n_init= 25, random_state= 1234)
    km.fit(customers_scaled)
    wcss.append(km.inertia_)

wcss_series = pd.Series(wcss, index= range (2,11))

plt.figure(figsize=(8, 6) )
ax = sns.lineplot (y = wcss_series, x = wcss_series.index)
ax = sns.scatterplot (y = wcss_series, x = wcss_series.index, s = 150)
ax = ax.set(xlabel = 'Number of Clusters (k)',
            ylabel = 'Within Cluster Sum of Squares (WCSS)')
#plt.show()


# The Average Silhouette Score

from sklearn.metrics import silhouette_score

silhouette = []
for k in range(2, 11):
        km = KMeans(n_clusters=k, n_init= 25, random_state= 1234)
        km.fit(customers_scaled)
        silhouette.append(silhouette_score(customers_scaled, km.labels_))
        
silhouette_series = pd.Series(silhouette, index= range(2,11))

plt.figure(figsize=(8, 6))
ax = sns.lineplot(y = silhouette_series, x=silhouette_series.index)
ax = sns.scatterplot(y= silhouette_series, x=silhouette_series.index, s=150)
ax = ax.set(xlabel = 'Number of Clusters (k)',
            ylabel = 'Average Silhouette Score')
#plt.show()

# The Calinski harabsz Score

from sklearn.metrics import calinski_harabasz_score

calinski = []
for k in range(2, 11):
    km= KMeans(n_clusters= k, n_init= 25, random_state=1234)
    km.fit(customers_scaled)
    calinski.append(calinski_harabasz_score(customers_scaled, km.labels_))

calinski_series = pd.Series(calinski, index= range(2,11))

plt.figure(figsize=(8,6))
ax = sns.lineplot(y = calinski_series, x=calinski_series.index)
ax = sns.scatterplot(y= calinski_series, x=calinski_series.index, s=150)
ax = ax.set(xlabel = 'Number of Clusters (k)',
            ylabel = 'Calinski Harabasz Score')
#plt.show()

###########################
# 6) Analyze and Interpret the Clusterd

km= KMeans(n_clusters= 5, n_init= 25, random_state= 1234)
km.fit(customers_scaled)

cluster_centers = pd.DataFrame(km.cluster_centers_, columns= ['Income', 'SpendingScore'])

# Set the figure size
plt.figure(figsize=(10,8))

#Plot the Clusters

ax = sns.scatterplot(data=customers_scaled, 
                     x= 'Income',
                     y= 'SpendingScore',
                     palette= 'colorblind',
                     alpha = 0.8,
                     s= 150,
                     legend= False)
#plt.show()

#PLot the Centroids
ax = sns.scatterplot(data=cluster_centers,
                     x= 'Income',
                     y= 'SpendingScore',
                     hue= cluster_centers.index,
                     palette= 'colorblind',
                     s= 600,
                     marker= 'D',
                     ec= 'black',
                     legend= False)
plt.show()

# Add centroid Labels
for i in range(len(cluster_centers)):
                plt.text(x= cluster_centers.Income[i],
                         y= cluster_centers.SpendingScore[i],
                         s= i,
                         horizontalalignment= 'center',
                         verticalalignment= 'center',
                         size= 15,
                         weight= 'bold',
                         color= 'white'
                         )
plt.show()

customers ['Cluster'] = km.labels_.tolist()
print(customers.head())

customers = pd.get_dummies(customers, columns= ['Gender'])
print(customers.head(10))

# descriptive statistics

print(
        customers.agg(
        {        
        'Gender_Female' : 'mean',
        'Gender_Male' : 'mean',
        'Age' : 'median',
        'Income' : 'median',
        'SpendingScore' : 'median'}
        ).round(2)
)

print(
        customers.groupby('Cluster').agg(
        {        
        'Gender_Female' : 'mean',
        'Gender_Male' : 'mean',
        'Age' : 'median',
        'Income' : 'median',
        'SpendingScore' : 'median'}
        ).round(2)
)

