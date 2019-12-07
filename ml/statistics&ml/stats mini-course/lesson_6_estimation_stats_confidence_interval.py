#from: https://machinelearningmastery.com/statistics-for-machine-learning-mini-course/?unapproved=514048&moderation-hash=59263e27d9f1381cae7e46cf9bbf8f8f#comment-514048
" Confidence Interval ---------------------------------------------------------------------######################"
# calculate the confidence interval
from statsmodels.stats.proportion import proportion_confint

# calculate the interval
#88 correct predictions for 100 instance with 0.95 confidence interval (i.e. significance level of 0.05)
lower, upper = proportion_confint(88, 100, 0.05)
print('lower=%.3f, upper=%.3f' % (lower, upper))