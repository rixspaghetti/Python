from scipy.stats import t, norm
import math

#given data 
n = 7
sample_mean = 315
sample_std_dev = 16
hypothesized_mean = 300
significance_level = 0.05
true_mean = 305

# part (a) - calculate the t-statistic and p-value
# t = (sample_mean - hypothesized_mean) / (sample_std_dev / sqrt(n))
t_statistic = (sample_mean - hypothesized_mean) / (sample_std_dev / math.sqrt(n))

# calculating the one-tailed p-value for the t-statistic with (n-1) degrees
p_value = 1 - t.cdf(t_statistic, df=n-1)

# output
print("\nPart(a):")
print(f"t_statistic = {t_statistic:.4f}")
print(f"p_value = {p_value:.4f}\n")

# part (b) compute the power of the test if the true strength is 305 watts

#calculate the effect size (cohens d):
# d = (true_mean - hypothesized_mean) / sample_std_dev
effect_size = (true_mean - hypothesized_mean) / sample_std_dev

# Non-centranality parameter (delta) for the t-distribution
# delta = effect_size * sqrt(n)
non_centranality_param = effect_size * math.sqrt(n)

# Calculate the critical t-value for the given significance level (one-tailed)
t_critical = t.ppf(1 - significance_level, df=n-1)

# calculate the power 
# power is the probability of correctly rejecting the null hypothesis
# it is computed as 1 - P(Type II error), where P(Type II error) is based on
# the non-centranality paremeter and the critical t-value
power = 1 - t.cdf(t_critical - non_centranality_param, df=n-1)

# output
print("\nPart(b):")
print(f"Effect size (d) = {effect_size:.4f}")
print(f"Power of the test = {power:.4f}")






