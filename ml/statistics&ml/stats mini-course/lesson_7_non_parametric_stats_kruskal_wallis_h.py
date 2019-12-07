#https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/
"Kruskal-Wallis H Test ------------------------------------------------------------------------------------###"
""" Tests if the distribuitions of two or more independent samples are equal or not """

from scipy.stats import kruskal

#n can be different (n(data1) and n(data2))
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169, 0.33, -0.44]

stat, p = kruskal(data1, data2)
print('stat=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
	print('Probably the same distribution')
else:
	print('Probably different distributions')