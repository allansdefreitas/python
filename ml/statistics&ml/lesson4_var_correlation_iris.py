#from: https://machinelearningmastery.com/statistics-for-machine-learning-mini-course/?unapproved=514046&moderation-hash=5fc38cc2acef95443b0212df74625b5c#comment-514046
from sklearn import datasets
iris = datasets.load_iris()

# calculate correlation coefficient
from scipy.stats import pearsonr

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
sepal_width = X[:,1]

print(sepal_lenghts)
type(sepal_lenghts)
print(sepal_lenghts.shape)
print(sepal_lenghts.size)


print(sepal_width)
type(sepal_width)
print(sepal_width.shape)
print(sepal_width.size)


# calculate Pearson's correlation
corr, p = pearsonr(sepal_lenghts, sepal_width)

# display the correlation: in this case, NEGATIVE CORRELATION
print('Pearsons correlation: %.3f' % corr)