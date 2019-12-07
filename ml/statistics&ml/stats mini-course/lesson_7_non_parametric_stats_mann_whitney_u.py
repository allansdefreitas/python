#from: https://machinelearningmastery.com/statistics-for-machine-learning-mini-course/?unapproved=514048&moderation-hash=59263e27d9f1381cae7e46cf9bbf8f8f#comment-514048
"Mann-Whitney U test ------------------------------------------------------------------------------------###"
""" It is equivalent to Student's T test (in Gaussian distribution data) to check if the data are drawn from 
    the same distribution """
 # example of the mann-whitney u test
from numpy.random import seed
from numpy.random import rand
from scipy.stats import mannwhitneyu

# seed the random number generator
seed(1)

# generate two independent samples
data1 = 50 + (rand(100) * 10)
data2 = 51 + (rand(100) * 10)

# compare samples
stat, p = mannwhitneyu(data1, data2)
print('Statistics=%.3f, p=%.3f' % (stat, p))

# interpret
alpha = 0.05
if p > alpha:
	print('Same distribution (fail to reject H0)')
else:
	print('Different distribution (reject H0)')