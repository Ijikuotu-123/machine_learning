# gradient descend is used to solve the problem of dummy variable

import numpy as np
import matplotlib.pyplot as plt

N = 10
D = 3
X =np.zeros((N,D))
X[:,0] = 1
X[:5,1] = 1
X[5:,2] = 1

Y = np.array([0]*5 + [1]*5) # 5 zeroes and 5 onces

#w =np.linalg.solve(X.T.dot(X), X.T.dot(Y))  # our regular solution will give an error instead use gradient descend

cost =[]

w = np.random.randn(D)/np.sqrt(D)
learning_rate = 0.01

for t in range(1000):
    yhat = X.dot(w)
    delta = Y -yhat
    w = w - learning_rate*(X.T.dot(delta))
    mse = delta.dot(delta)/N
    cost.append(mse)

print(w)
plt.plot(cost)
plt.show()