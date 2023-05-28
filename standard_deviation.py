# -*- coding: utf-8 -*-
"""Standard_Deviation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c_VUIgs5EEoXhRD27aO1hUpC5UgDq3aj
"""

!pip install numpy statistics

import numpy as np
import statistics

# Create a sample dataset
data = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10]

# Calculate the mean
mean = np.mean(data)
print("Mean:", mean)

# Calculate the median
median = np.median(data)
print("Median:", median)

# Calculate the mode
mode = statistics.mode(data)
print("Mode:", mode)

import matplotlib.pyplot as plt

plt.hist(data, bins=5)  

# Add labels and title
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Histogram of Age')

# Display the histogram
plt.show()

import matplotlib.pyplot as plt

# Data
x = ['Value 1', 'Value 2', 'Value 3', 'Value 4', 'Value 5']
y = [1,2,3,4,5]


# Create a bar chart
plt.bar(x, y)
plt.xlabel('Values')
plt.ylabel('Counts')
plt.title('Bar Chart')

plt.show()

import numpy as np
from scipy import stats

# Create a sample dataset
data = [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10]

# Calculate z-scores
z_scores = stats.zscore(data)

print("Z-Scores:", z_scores)

import matplotlib.pyplot as plt

# Custom data
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Create a histogram
plt.hist(data, bins=5, edgecolor='black')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')

plt.show()