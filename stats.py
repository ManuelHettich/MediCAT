import matplotlib.pyplot as plt
import numpy as np

# Provided data distributions
distribution1 = [
    0.1, 0.65, 0.8, 0.5, 0.7, 0.6, 0.5, 0.75, 0.85, 0.4,
    0.8, 0.9, 0.95, 0.9, 0.9, 0.8, 0.6, 0.85, 0.7, 0.65,
    0.75, 0.8, 0.6, 0.85
]

distribution2 = [
    0.4, 0.7, 0.9, 0.5, 0.85, 0.7, 0.75, 0.9, 0.95, 0.8,
    0.8, 0.85, 0.95, 0.9, 0.7, 0.75, 0.6, 0.85, 0.6, 0.5,
    0.7, 0.85, 0.6, 0.9
]

# Convert the lists to numpy arrays for better handling
dist1 = np.array(distribution1)
dist2 = np.array(distribution2)

# Calculate basic statistics
mean1 = np.mean(dist1)
mean2 = np.mean(dist2)
std1 = np.std(dist1)
std2 = np.std(dist2)
median1 = np.median(dist1)
median2 = np.median(dist2)

print(mean1, mean2, std1, std2, median1, median2)

# Plot the distributions
plt.hist(dist1, bins=10, alpha=0.5, label='dist1')
plt.hist(dist2, bins=10, alpha=0.5, label='dist2')
plt.legend(loc='upper right')
plt.show()
