""" is used to when D is greater than N. It is used when the weights of most of the features are not too
important.. i.e close to zero.
we would generate a data whose input is a fat matrix(D is large) and y depends on only few of the features"""

import numpy as np
import matplotlib.pyplot as plt

N =50
D=50

X = (np.random.random((N,D)) -0.5)*10 # this is centred around -5 to +5

true_w = np.array([1, 0.5, -0.5] + [0]*(D-3))  # last 47 isn't important

Y = X.dot(true_w) + np.random.randn(N)*0.5

costs =[]
w = np.random.randn(D)/np.sqrt(D)
learning_rate = 0.001
l1=10.0
for t in range(500):
    yhat = X.dot(w)
    delta = yhat-Y
    w = w - learning_rate*(X.T.dot(delta) + l1*np.sign(w))
    mse = delta.dot(delta)/N
    costs.append(mse)

plt.plot(costs)
plt.show()

print (w)

