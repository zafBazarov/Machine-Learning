### DATA PREPARATION stage

# * It is a process which intends to modify your data 
# so it works for the type of machine learning you intend to do.

# Common data quality issue: 
# 1) Missing Data - solutions: 
# - remove missing values
# - label the missing data with NA or -1 and so on.
# - imputation = The use of a systematic approach to fill in missing data by using the most probable substitute values.
    #++ There several imputation methods
    # Median Imputation = Replace missing values with Median.

# 2) Outliers = are significantly different values from a dataset.
#   we should understand why do they exist?

# 3) Class Imbalance
# - Occurs when the distribution of values for the class is not uniform
# - Class imbalance is a well-known problem in ML
# - If not properly accounted for, class imbalance can lead to rather misleading predictions
#   +++ Solution 1: 
            # randomly remove some of the instances of the the majority class #
            # in an attempt to even the class distribution. 
