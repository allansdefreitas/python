#https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/
"Kendal's Rank Correlation ---------------------------------------------------------------------###########"
""" Tests if two samples has a monotonic relationship or not. i.e.  don't vary """

from scipy.stats import kendalltau

data1 = [0.873, 2.817, 0.121, -0.945, -0.055, -1.436, 0.360, -1.478, -1.637, -1.869]
data2 = [0.353, 3.517, 0.125, -7.545, -0.555, -1.536, 3.350, -1.578, -3.537, -1.579]

stat, p = kendalltau(data1, data2)
print('stat=%.3f, p=%.3f' % (stat, p))

alpha = 0.05
if p > alpha:
	print('Probably independent')
else:
	print('Probably dependent')