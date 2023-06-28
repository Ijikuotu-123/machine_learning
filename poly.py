import numpy as np
import matplotlib.pyplot as plt

# load data # data has 2 columns
X = []
Y = []
for line in open('data_poly.csv'):
    x, y = line.split(',')
    x=float(x)  
    X.append(x, x*x, 1)
    Y.append(float(y))

# turn X and Y into numpy arrays

X = np.array(X)
Y = np.array(Y)

# let's plot the data to see what it looks like
plt.scatter (X[:,1],Y)
plt.show()

# calculate weights
w = np.linalg.solve(np.dot(X.T,X),np.dot(X.T,Y))
Yhat = np.dot(X,w)

# plot it all together
plt.scatter(X[:.1],Y)
plt.plot(sorted(X[:.1]),sorted(Yhat))   # sorted is added to ensure that the points are where they should be
plt.show()

# to calculate r-squared. it does not change because it depends only on y and yhat
d1 = y -yhat
d2 = y - y.mean()
r2 = 1 -d1.dot(d1)/d2.dot(d2)
print (r2)
