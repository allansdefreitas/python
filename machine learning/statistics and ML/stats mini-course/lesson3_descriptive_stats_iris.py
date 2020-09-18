import numpy as np
import math
from sklearn import datasets
iris = datasets.load_iris()

#Attributes
#1. sepal length in cm
#2. sepal width in cm
#3. petal length in cm
#4. petal width in cm

X = iris.data
print(X.size)
print(X.shape)

#column 0..all lines
sepal_lenghts = X[: , 0]

print(sepal_lenghts.size)
print(sepal_lenghts.shape)

#same thing was done above
sepal_width = X[:,1]
petal_lenght = X[:,2]
petal_width = X[:,3]

#Calculate the mean, variance and standard deviation "by hand"! -------------##
#Mean "by hand" -------------------##
def mean_by_hand(data):
    i_arr_summation = 0
    for x in np.nditer(data):
        i_arr_summation += x
    
    size_data = data.size
    mean_data = i_arr_summation / size_data
    return mean_data

#Variance "by hand" -------------------------------------------------------###
def variance_by_hand(data, mean_data, n_data):
    sum_var = 0
    for x in np.nditer(data):
        i_var = x - mean_data #variance (xi - mi)
        i_var *= i_var # ^2
        sum_var += i_var #summation
    variance = (1/n_data) * sum_var
    return variance


#Standard deviation "by hand". Are you serious?! --------------------------####
def standard_dev_by_hand(variance):
    standard_dev = math.sqrt(variance) #or variance**0.5
    return standard_dev



#Calling the functions to calculate mean, var and std -----------##############
#Mean ------------------------------------------------####
mean_sepal_lenghts = mean_by_hand(sepal_lenghts)
print("mean sepal_lenght:", mean_sepal_lenghts)
print("NUMPY mean sepal_lenght:", np.mean(sepal_lenghts))

#Variance ------------------------------------------------####
n_sepal_lenghts = sepal_lenghts.size
var_sepal_lenghts = variance_by_hand(sepal_lenghts, mean_sepal_lenghts, n_sepal_lenghts)
print("var sepal_lenght:", var_sepal_lenghts)
print("NUMPY var sepal_lenght:", np.var(sepal_lenghts))

#Standard deviation--------------------------------------####
std_sepal_lengths = standard_dev_by_hand(var_sepal_lenghts)
print("std sepal_lenght:", std_sepal_lengths)
print("NUMPY std sepal_lenght:", np.std(sepal_lenghts))







