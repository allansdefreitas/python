#https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/
"Friedman Test ------------------------------------------------------------------------------------###"
""" Tests if the distribuitions of two or more paired samples are equal or not """
# Example of the Friedman Test
from scipy.stats import friedmanchisquare

# N of data must be equal!
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]
data3 = [-0.208, 0.696, 0.928, -1.148, -0.213, 0.229, 0.137, 0.269, -0.870, -1.204]

stat, p = friedmanchisquare(data1, data2, data3)
print('stat=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
