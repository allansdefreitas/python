#https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/
"Chi-Squared Test ---------------------------------------------------------------------###########"
""" Tests if two categorical variable are related or independent """

from scipy.stats import chi2_contingency
table = [[10, 20, 30],[6,  9,  17]]

stat, p, dof, expected = chi2_contingency(table)
print('stat=%.3f, p=%.3f' % (stat, p))

alpha = 0.05
if p > alpha:
	print('Probably independent')
else:
	print('Probably dependent')