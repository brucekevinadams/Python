# Python 3 code
# Bruce Adams
# austingamestudios.com
# ezaroth@gmail.com
# Program problem from Hackerrank.com 
# In a certain plant, the time taken to assemble a car is a random variable, X, 
# having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours.
# What is the probability that a car can be assembled at this plant in:
#
#    Less than 19.5 hours?
#    Between and 20 and 22 hours?
# Input Format
#
# There are 3 lines of input (shown below):
#
# 20 2
# 19.5
# 20 22
#
# The first line contains space-separated values denoting the respective mean and standard deviation for X.
# The second line contains the number associated with question 1. The third line contains 2 space-separated
# values describing the respective lower and upper range boundaries for question 2.
#
# Output Format
#
# There are two lines of output. Your answers must be rounded to a scale of decimal places (i.e., format):
#
#    On the first line, print the answer to question 1 (i.e., the probability that a car can be assembled in less than 19.5 hours)
#    On the second line, print the answer to question 2 (i.e., probability that a car can be assembled in between 20 to 22 hours)

import math
mean, std = 20, 2
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
print('{:.3f}'.format(cdf(19.5)))
# Between 20 and 22
print('{:.3f}'.format(cdf(22) - cdf(20)))
