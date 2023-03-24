import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.normal(size=1000)

# Calculate the cumulative distribution
sorted_data = np.sort(data)
cumulative = np.cumsum(sorted_data)

# Plot the cumulative distribution
plt.plot(sorted_data, cumulative)
plt.title('Cumulative Distribution')
plt.xlabel('Data')
plt.ylabel('Cumulative')
plt.show()



import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.normal(size=1000)

# Create histogram
n, bins, patches = plt.hist(data, bins=30, density=True, cumulative=True)

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Cumulative Probability')
plt.title('Cumulative Distribution Histogram')

# Show plot
plt.show()
plt.legend(loc='lower right')






def correlation_function(config, k):
    """
    Calculate the correlation function for the Ising model.
    """
    L = len(config)
    corr = 0
    for i in range(L):
        for j in range(L):
            corr += config[i][j] * config[(i+k)%L][j]
    corr /= L**2
    return corr


    
config = [[1, -1, 1], [-1, 1, -1], [1, -1, 1]]
k = 1
corr = correlation_function(config, k)
print(corr)
