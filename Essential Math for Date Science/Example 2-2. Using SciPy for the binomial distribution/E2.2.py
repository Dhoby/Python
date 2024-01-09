from scipy.stats import binom
n = 10
p = 0.9
for k in range(n + 1):
     probability = binom.pmf(k, n, p)
     print("{0} - {1}".format(k, probability))

