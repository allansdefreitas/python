#https://machinelearningmastery.com/statistical-hypothesis-tests-in-python-cheat-sheet/
"Augmented Dickey-Fuller Unit Root Test ---------------------------------------------------------------###########"
""" Tests if a time series is stationary or not. i.e. fixed, immobile """
from statsmodels.tsa.stattools import adfuller

data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

stat, p, lags, obs, crit, t = adfuller(data)
print('stat=%.3f, p=%.3f' % (stat, p))

if p > 0.05:
	print('Probably not Stationary')
else:
	print('Probably Stationary')