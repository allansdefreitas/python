" Student's T test for independent samples -----------------------------------------##############################"

# Example of the Student's t-test
from sklearn import datasets
iris = datasets.load_iris()
from scipy.stats import ttest_ind #INDEPENDENT TTest 


#TTest with random dataset --------------------------------------------------#
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]

stat, p = ttest_ind(data1, data2)

print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('H0: Probably the same distribution')
else:
	print('H1: Probably different distributions')
    
    
#TTest wiht iris dataset ----------------------------------------------------#
    
#Iris dataset attributes
#1. sepal length in cm
#2. sepal width in cm
#3. petal length in cm
#4. petal width in cm

X = iris.data

#column 0..all lines
sepal_lenghts = X[: , 0]
sepal_width = X[:,1]

stat_iris, p_iris = ttest_ind(sepal_lenghts, sepal_width)
alpha = 0.05

if(p_iris > alpha):
     	print('H0: Probably the same distribution')
else:
	print('H1: Probably different distributions')