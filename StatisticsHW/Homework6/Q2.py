import scipy.stats as stats

#given data 
mu = 12         #Population mean under H0
sample_mean = 11.25 # observerd sample mean
sigma = 0.5     # population standard deviation
n = 4           # sample size 

# calculate the z test statistic 
z_score = (sample_mean - mu) / (sigma / (n**0.5))

# calculate the p-value for a left-tailed test
# cumulative distribution function(CDF) of the standard normal distribution
p_value = stats.norm.cdf(z_score)

print(f"Z-score: {z_score:.5f}")
print(f"P-value: {p_value:.5f}")


