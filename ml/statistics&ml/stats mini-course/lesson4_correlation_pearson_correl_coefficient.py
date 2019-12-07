#from: https://machinelearningmastery.com/statistics-for-machine-learning-mini-course/?unapproved=514046&moderation-hash=5fc38cc2acef95443b0212df74625b5c#comment-514046

# calculate correlation coefficient
from numpy.random import seed
from numpy.random import randn
from scipy.stats import pearsonr

# seed random number generator
seed(1)

# prepare data
data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)

# calculate Pearson's correlation
corr, p = pearsonr(data1, data2)

# display the correlation: in this case, strongly positive correlation
print('Pearsons correlation: %.3f' % corr)