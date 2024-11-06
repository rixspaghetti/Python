from scipy.stats import norm

# given paramaters
mu_0 = 12       # Hypothesized mean
sigma = 0.5     # Population standard deviation
n = 4           # sample size
alpha_critical_value = 11.5 # Critical value for Type I error calculation

# Calculate standard error
standard_error = sigma / (n ** 0.5)

# Part (a): Type I Error Probability (alpha)
# When H0 is true, mu = 12
z_alpha = (alpha_critical_value - mu_0) / standard_error
alpha = norm.cdf(z_alpha)

# Part (b): Type II Error Probability (beta) for mean of 11.26
mu_1_b = 11.26
z_beta_b = (alpha_critical_value - mu_1_b) / standard_error
beta_b = 1 - norm.cdf(z_beta_b)

# Part (c): Type II Error Probability (beta) for true mean of 11.5
mu_1_c = 11.25
z_beta_c = (alpha_critical_value - mu_1_c) / standard_error
beta_c = 1 - norm.cdf(z_beta_c)

alpha, beta_b, beta_c