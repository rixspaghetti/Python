from scipy.stats import norm 
import math

# given values
mu = 175        # hypothesized mean
sigma = 20      # pop standard dev
alpha = 0.05    # significance level 
n = 16          # sample size

# calculate the z ciritical value for a 0.05 significance level
z_alpha = norm.ppf(1-alpha)

# calculate the boundary for the sample mean
critical_value = mu + z_alpha * (sigma/ math.sqrt(n))

print(f"{z_alpha:.2f}")
print(f"{critical_value:.1f}")
