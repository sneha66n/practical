from matplotlib import pyplot as plt

# Ensure x and y have the same number of elements
x = [2, 4, 8]  # Adjusted to match length of y
y = [218, 8, 2]

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Graph')  # Added quotes
plt.bar(x, y, label="Graph", color='r', width=0.5)
plt.legend()
plt.show()
