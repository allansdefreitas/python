#https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/
"Wilcoxon Signed-Rank test ------------------------------------------------------------------------------------###"
""" Tests if the distribuitions of two paired samples are equal or not """

from scipy.stats import wilcoxon
#Obs.: THE SIZE OF DATA MUST BE EQUAL! I.E n(DATA1) == n(DATA2)
data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [1.142, -0.432, -0.938, -0.729, -0.846, -0.157, 0.500, 1.183, -1.075, -0.169]

stat, p = wilcoxon(data1, data2)
print('stat=%.3f, p=%.3f' % (stat, p))
alpha = 0.05
if p > alpha:
	print('Probably the same distribution')
else:
	print('Probably different distributions')
    
