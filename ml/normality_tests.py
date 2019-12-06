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


isGaussian(sepal_width)
isGaussian(petal_lenght)
isGaussian(petal_width)


#Is it sepal lenghts drawn from a gaussian distribution?

def isGaussian(data):
        
    # histogram plot --------------------------------------------------------------
    print("Histogram plot -------------------------------------")
    pyplot.hist(data)
    pyplot.show()
    
    
    #QQPlot ----------------------------------------------------------------------
    print("QQ plot -------------------------------------")
    from statsmodels.graphics.gofplots import qqplot
    # q-q plot
    qqplot(data, line='s')
    pyplot.show()
    
    #shapiro wilk-test -----------------------------------------------------------
    print("Shapiro-Wilk test -------------------------------------")
    from scipy.stats import shapiro
    stat, p = shapiro(data)
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    
    # interpret
    alpha = 0.05
    
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')
        
    #D'Agostino's K^2 Test --------------------------------------------------------
    print("D'Agostino's K^2 test -------------------------------------")
    from scipy.stats import normaltest
    # normality test
    stat, p = normaltest(data)
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    
    if p > alpha:
        print('Sample looks Gaussian (fail to reject H0)')
    else:
        print('Sample does not look Gaussian (reject H0)')
    
    #Anderson-Darling Test --------------------------------------------------------
    print("Anderson-Darling test -------------------------------------")
    from scipy.stats import anderson
    # normality test
    result = anderson(data)
    print('Statistic: %.3f' % result.statistic)
    p = 0
    for i in range(len(result.critical_values)):
        sl, cv = result.significance_level[i], result.critical_values[i]
        if result.statistic < result.critical_values[i]:
            print('%.3f: %.3f, data looks normal (fail to reject H0)' % (sl, cv))
        else:
            print('%.3f: %.3f, data does not look normal (reject H0)' % (sl, cv))
            
    #A failure of one normality test means that your data is not normal. As simple as that!..so...
