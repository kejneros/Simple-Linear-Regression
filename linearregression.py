import numpy as np
import matplotlib.pyplot as plt
import random

# Since the y value is randomly generated,
# I will use random.seed to ensure that we have
# 1 result in our simulation
random.seed(12345)


# Initialize data
X_array = []
for i in range(100):
    X_array.append(i)
X = np.array(X_array).reshape(-1,1)
Y_array = []

# Generate a normal Y value distribution with mean
# 50 and standard deviation 1
for number in range(len(X)):
    number = np.random.normal(50,0.1)
    Y_array.append(number)

Y = np.array(Y_array)
# print(X)


# Find the mean value of X and y
x_mean = np.mean(X)
y_mean = np.mean(Y)
# print(X-mean)

# initializing our inputs and outputs


# total number of values
n = len(X)
# using the formula to calculate the b1 and b0
numerator = 0
denominator = 0
for i in range(n):
    numerator += (X[i] - x_mean) * (Y[i] - y_mean)
    denominator += (X[i] - x_mean) ** 2

b1 = numerator / denominator
b0 = y_mean - (b1 * x_mean)
#print(b1, b0)


#plotting values
x_max = np.max(X) + 10
x_min = np.min(X)

#calculating line values of x and y
x = np.linspace(x_min, x_max, 100)
y = b0 + b1 * x

# plot the regression line
plt.plot(x, y, label='linear regression')
# plot the data point
plt.scatter(X, Y, color='red', label='data points')

# plot the labels
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
