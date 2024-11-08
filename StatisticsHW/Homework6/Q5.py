from scipy.stats import norm
import math

# given values 
mu_0 = 5        # hypothesized mean under H0
sigma = 0.42    # population standard deviation
n = 5           # sample size 
alpha_region_low = 4.85
alpha_region_high = 5.17
mu_alt = 5.1 

#(a) calculate z-scores for the acceptance region boundaries under H0
z_low = (alpha_region_low - mu_0) / (sigma / math.sqrt(n))
z_high = (alpha_region_high - mu_0) / (sigma / math.sqrt(n))

# calculate alpha (significance level)
alpha = (1 - norm.cdf(z_high) + norm.cdf(z_low))

#(b) calculate the power of the test under the alternative mean
z_low_alt = (alpha_region_low - mu_alt) / (sigma / math.sqrt(n))
z_high_alt = (alpha_region_high - mu_alt) / (sigma / math.sqrt(n))

#calculate power
power = (1 - norm.cdf(z_high_alt)) + norm.cdf(z_low_alt)

print(f"{alpha:.4f}")
print(f"{power:.4f}")