#adapted from: https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/
" Paired Student's T test --------------------------------------------------------##############################"

# Example of the Paired Student's t-test with  random data -----------------###################
from scipy.stats import ttest_rel #real means "paired samples" (i.e. not independent, related)

data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
stat, p = ttest_rel(data1, data2)

print('stat=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
    
    
# Example of the Paired Student's t-test with Iris dataset -----------------###################
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

stat_iris, p_iris = ttest_rel(sepal_lenghts, sepal_width)
alpha = 0.05
if p > alpha:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
    
    
#one more test:
petal_lenght = X[:,2]
petal_width = X[:,3]

stat_iris, p_iris = ttest_rel(petal_lenght, petal_width)
alpha = 0.05
if p > alpha:
	print('Probably the same distribution')
else:
	print('Probably different distributions')

#one more test. I sure!
stat_iris, p_iris = ttest_rel(sepal_lenghts, petal_lenght)

if p_iris > alpha:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
    
    