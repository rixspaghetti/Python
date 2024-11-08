import math 
from scipy.stats import norm 

# given values
mu = 175        # hypothesized mean
sample_mean =  190# observed sample mean
sigma = 20      # population standard deviation
n = 10

# calculate the test statistic z0
z_0 = (sample_mean - mu) / (sigma / math.sqrt(n))

# right tailed p-value
p_value = 1 - norm.cdf(z_0)

print(f"{z_0:.5f}, {p_value:.5f}")