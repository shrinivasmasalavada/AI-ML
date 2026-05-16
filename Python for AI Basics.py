import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Matrix operations
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Addition:\n", A + B)
print("Multiplication:\n", A @ B)

# Random data
x = np.random.rand(100)
y = 2*x + 1

plt.scatter(x, y)
plt.title("Simple AI Data Visualization")
plt.show()