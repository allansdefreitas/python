from sklearn import datasets
from matplotlib import pyplot
iris = datasets.load_iris()

#Attributes
#1. sepal length in cm
#2. sepal width in cm
#3. petal length in cm
#4. petal width in cm

X = iris.data
print(X.size)
print(X.shape)

sepal_lenghts = X[: , 0]

print(sepal_lenghts.size)
print(sepal_lenghts.shape)

sepal_width = X[:,1]
petal_lenght = X[:,2]
petal_width = X[:,3]

#Is it sepal lenghts drawn from a gaussian distribution?

# histogram plot --------------------------------------------------------------
pyplot.hist(sepal_lenghts)
pyplot.show()


#QQPlot ----------------------------------------------------------------------
from statsmodels.graphics.gofplots import qqplot
# q-q plot
qqplot(sepal_lenghts, line='s')
pyplot.show()

#shapiro wilk-test -----------------------------------------------------------
from scipy.stats import shapiro
stat, p = shapiro(sepal_lenghts)
print('Statistics=%.3f, p=%.3f' % (stat, p))

# interpret
alpha = 0.05

if p > alpha:
    print('Sample looks Gaussian (fail to reject H0)')
else:
    print('Sample does not look Gaussian (reject H0)')
    
#D'Agostino's K^2 Test --------------------------------------------------------
from scipy.stats import normaltest
# normality test
stat, p = normaltest(sepal_lenghts)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05

if p > alpha:
    print('Sample looks Gaussian (fail to reject H0)')
else:
    print('Sample does not look Gaussian (reject H0)')

#Anderson-Darling Test --------------------------------------------------------
from scipy.stats import anderson
# normality test
result = anderson(sepal_lenghts)
print('Statistic: %.3f' % result.statistic)
p = 0
for i in range(len(result.critical_values)):
    sl, cv = result.significance_level[i], result.critical_values[i]
    if result.statistic < result.critical_values[i]:
        print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
    else:
        print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))
        
#A failure of one normality test means that your data is not normal. As simple as that!..so...
