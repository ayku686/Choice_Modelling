import matplotlib.pyplot as plt
import numpy as np

# Given probabilities
prob_av1 = [
    0.401, 0.341, 0.122, 0.013, 0.222, 0.432, 0.004, 0.002, 0.116, 0.087
]
prob_av2 = [
    0.231, 0.622, 0.743, 0.976, 0.385, 0.478, 0.952, 0.992, 0.638, 0.832
]
prob_av3 = [
    0.366, 0.036, 0.133, 0.009, 0.392, 0.089, 0.042, 0.004, 0.244, 0.080
]

# Data points for x-axis (indices of data points)
data_points = range(len(prob_av1))

# Width of the bars
bar_width = 0.25

# Plotting the three bars
plt.figure(figsize=(10, 6))

plt.bar(data_points, prob_av1, width=bar_width, label='AV1', alpha=0.7)
plt.bar([p + bar_width for p in data_points], prob_av2, width=bar_width, label='AV2', alpha=0.7)
plt.bar([p + 2*bar_width for p in data_points], prob_av3, width=bar_width, label='AV3', alpha=0.7)

# Adding labels and title
plt.xlabel('Data Points')
plt.ylabel('Probabilities')
plt.title('Probabilities of Alternatives AV1, AV2, AV3')
plt.xticks([p + bar_width for p in data_points], data_points)
plt.legend()

# Showing the plot
plt.show()
