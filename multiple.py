# multiple linear regression raises when more than one factor determines the output
# x is represented as a vector since it can contain multiple numbers and not a scalar
# Dimensionality == size of x , represented by the letter D
# w is also of size D
# our model:
           
y_hat = W^T + b

# BIAS_TERM
# we can also absorb b into w by appending a 1 to the feature vector x
# rename b to W0, and append x0 which is always 1






# CODING
import numpy as np
from mpl_toolkits.mplot3d import Axes3D   # for 3D drawing
import matplotlib.pyplot as plt

# load data
X = []
Y = []
for line in open('data_2.csv'):
    x1, x2, y = line.split(',')
    X.append([float(x1),float(x2),1])  # the one stands for x0 is always 1
    Y.append(float(y))

# turn X and Y into numpy arrays

X = np.array(X)
Y = np.array(Y)

# let's plot the data to see what it looks like
fig = plt.figure()
ax =fig.add_subpot(111,projection='3d')
ax.scatter(X[:,0],X[:,1], Y)
plt.show()

# calcualte weights
w = np.linalg.solve(np.dot(X.T,X),np.dot(X.T,Y))
Yhat = np.dot(X,w)

# to calculate r-squared
d1 = y -yhat
d2 = y - y.mean()
r2 = 1 -d1.dot(d1)/d2.dot(d2)
print (r2)
