""" Confidence interval - Estimate a populational parameter: MEAN: ------------------------------------ ####



n > 30 (Gauss, Z): 
CI(Mean) = sample_mean +- (Z (confidence_level/2) * sample_std/ sqrt(sample_n)) """

from scipy.stats import sem, t
from scipy import mean
import math


confidence = 0.95
data = [1, 2, 3, 4, 5]

#sample size (n)
n = len(data)

#sample mean (X|)
mean = mean(data)

#sample standard deviation (s)
std_err = sem(data)

"""
#n <= 30 (Student's T): 
The same thing above. The only difference is that we change Z for T
    CI(Mean) = sample_mean +- (T (confidence_level/2) * sample_std/ sqrt(sample_n))"""

#calculate T
degrees_of_freedom = n -1
h = (std_err * t.ppf((1 + confidence) / 2, degrees_of_freedom) ) /  math.sqrt(n)

#start of interval
start = mean - h
print(start)

#end of interval
end = mean + h
print(end)

print("the interval is between %.3f and %.3f"% (start, end))

