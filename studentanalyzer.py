import numpy as np

# User input
scores_input = input("Enter scores separated by space: ")
scores = np.array(list(map(float, scores_input.split())))

# Calculations
average = np.mean(scores)
highest = np.max(scores)
lowest = np.min(scores)
std_dev = np.std(scores)

# Output
print("\n📊 Score Analysis:")
print(f"Average Score: {average:.2f}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Standard Deviation: {std_dev:.2f}")
