from scipy.stats import norm

alpha = 0.045

z_alpha = norm.ppf(alpha)

print(f"{z_alpha:.2f}")
