#### L2 regularization is used to pennalize the large weight and helps to overcome overfitting.
# it is neccessary when we have outliers in our data set
# J =Summation(y -yhat)*2 + lamba|w|*2
# |w|*2 = wTw = w1*2 + w2*2 + w3*2 .........+wd*2 

import numpy as np
import matplotlib.pyplot as plt


N = 50    # size of samples

X = np.linspace(0,10, N) # creating an array whose values are between 0 and 10 inclusive and are equally spaced
y = 0.5*X + np.random.randn(N)  # np.random.randn(N) means random noise. this wont make the result to be perfect

y[-1]=+30        # y[-1] is reffering to the last row . the two points are outliers
y[-2]=+30        # y[-2] is reffering to second to the last row

plt.scatter(X,y)
plt.show()

X = np.vstack([np.ones(50), X]).T # vstack is used for concantenation. it arranges the arrray row wise.
# T ensure vertical arrangement in the array. note: np.ones(50) is the constant term 

w_ml = np.linalg.solve(X.T.dot(X), X.T.dot(y))
yhat_ml = X.dot(w_ml)

plt.scatter(X[:,1], y)
plt.plot(X[:,1], yhat_ml)
plt.show()

l2 = 1000   # l2 penalty = 1000. this is the lamder
w_map = np.linalg.solve(l2*np.eye(2) + X.T.dot(X), X.T.dot(y))
yhat_map = X.dot(w_map)

plt.scatter(X[:,1], y)
plt.plot(X[:,1], yhat_ml)
plt.plot(X[:,1], yhat_map, label = "map")
plt.legend()   # this enables me to put the 2 line on the scatter plot at once
plt.show()





 