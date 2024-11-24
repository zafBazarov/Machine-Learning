#
## Topic: What is clustering? 

#** 1) Introduction

    # Clusering is one of the Unsupervised ML approach
    # 
    # The primary objective of clustering is to create: 
    # 1) clusters with high-intraclass similarity    
    # 2) clusters low high-intraclass similarity 
    # 
    # Clustering is someiteimes used in the domain of network security, as a way to detect anamoluos behavior
    #  in computer networks.Also used ofr automatically group or categorize documents based on similarity.
    #   is to segment customers in marketing purpose# 

# Hierarchical Clustering: 
#                       approach in which cluster boundaries are nested within other clusters
# 
# Partitional Clustering: 
#                       approach in which cluster boundaries are noneoverlapping
# 
# Overlapping Clustering: 
#                       approach in which the boundary of one vluster can overlap that of another
#
# Fuzzy Clustering: 
#                  approach in which membership is weighted between 0 and 1
#
# Density-Based Clustering: 
#                  approach in which membership is assigned based on the density of items within a region


##############
## ** 2) k-means clustering
                    # is a partitional cluster typpe.  
                    # K-Means algorithm calculates the Euclian distance each poit and each of the three cluster centers.
                    # 
                    #   Euclidean Distance: 
                    #                   is the straight-line distance between the coordinates of two points
                    #                   in multidimensional space.
                    #   Cluster Centroid: 
                    #                   is the average position of the items currently assigned to a cluster.


################################################
#** 3) Choosing the Right Number of Clusters (k) 
#   
#   We can choose an appropriate value for k: 
#       - Based on a priori knowledge or business requirements
# 
#       - Usinga rule of thumb, such as k = the square root of half the number of observations k= _/(n/2) 
# 
#       - Using one or more statistical measures more reasonable.
# 
#   STATISTICAL METHODS
#  
#   1) Within-Cluster Sum of Squares (WCSS):
#               - quantifies the degree of similiarity between items in a cluster.
#               - is the sum of the distances from each item in the cluster to the cluster centroid
#               - As the vaue of k inceases, the items within each cluster become closer and the WCSS becomes smaller
# 
# The Elbow Method:
#                   ** choose the k at the most significant inflection point between WCSS and the number of clusters. 
#                   this point is known as the elbow.
# 
#  2) The Average Silhouette method: 
#                  - of an items is a measure of how closely the items is matched with other items within the same cluster
#                   and how loosely it is matched with items in neighboring clusters. 
#                   
#                  - the higher the  silhouette value of an item, the more likely that it is in right cluster. 
#                       Silhouette values range from -1 to 1 
#                  
#                  - the k value corresponding to the highest average silhoette represents the optimal
#                       number of lcusters.  
# 
#      3) The Clinski-Harabasz Score
#                   - is an adjusted ratio of between-cluster sum of squares and the within-cluster som of squares.
#                   - the higher the score is, the denser and more separated the clusters are. 
#                   
#                   ** Choose the k value at the peak or the most significant inflection point or elbow.# 


################################################
##** 4) Why and When to use k-means clustering
# 
#       It simple,
#       can be applied to a wide set of problems, market segmentation, social network analysis and so on.
# 
# WEAKNESSES 
#           - It is not always clear what the best value for k should be
#           - It can be run multiple times, and have different results using a single dataset, we choose the hazard lowes WCSS.
#           - It is not good at creating nonspherical clusters.    
#           - Data with varying density does not work well with k-means clustering
#           - outliers impact the location of lcuster centers.
#           - it only works with numeric data. 
# # 