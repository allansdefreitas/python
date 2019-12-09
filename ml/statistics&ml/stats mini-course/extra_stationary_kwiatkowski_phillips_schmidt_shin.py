#https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/
"Kwiatkowski-Phillips-Schmidt-Shin ---------------------------------------------------------------###########"
""" Tests if a time series is stationary or not. i.e. fixed, immobile """
# Example of the Kwiatkowski-Phillips-Schmidt-Shin test
from statsmodels.tsa.stattools import kpss

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
stat, p, lags, crit = kpss(data)
print('stat=%.3f, p=%.3f' % (stat, p))

if p > 0.05:
	print('Probably not Stationary')
else:
	print('Probably Stationary')