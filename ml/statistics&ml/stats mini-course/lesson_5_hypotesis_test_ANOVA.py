#adapted from: https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/
" Analysist of Variance Test (ANOVA) --------------------------------------------------------##############################"
#Repeated Measures ANOVA Test ARE NOT CURRENTLY SUPPORTED IN PYTHON..do "by hand"!

# Example of the Analysis of Variance Test with random data ------------------------###########
from scipy.stats import f_oneway

data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
data3 = [-0.208, 0.696, 0.928, -1.148, -0.213, 0.229, 0.137, 0.269, -0.870, -1.204]
stat, p = f_oneway(data1, data2, data3)

print('stat=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
    
    
# Example of the Analysis of Variance Test with Iris dataset ------------------------############
from sklearn import datasets
iris = datasets.load_iris()

#Iris dataset attributes
#1. sepal length in cm
#2. sepal width in cm
#3. petal length in cm
#4. petal width in cm

X = iris.data

#column 0..all lines
sepal_lenghts = X[: , 0]
sepal_width = X[:,1]
petal_lenght = X[:,2]

stat_iris, p_iris = f_oneway(sepal_lenghts, sepal_width, petal_lenght)
print('stat=%.3f, p=%.3f' % (stat,p))
alpha = 0.05
if p_iris > alpha:
	print('Probably the same distribution')
else:
	print('Probably different distributions')