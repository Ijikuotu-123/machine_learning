# our data is an excel file. To read it we need to  do sudo  pip install xlrd to use pd.read_excel

# predicting systolic blood pressure from age and weight
# x1 = systolic blood pressure. This will be our y
# x2 = age in years  # input
# x3 = weight in pounds   # input

# we can see that BP has a linear relationship with both inputs

import matplotlibs.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('mlr02.xls')

X = df.as_matrix() # as_matrix is now be replaced with .values 
plt.scatter(X[:,1], X[:,0])  # we have picked age as x axis and BP as y axis
plt.show()

plt.scatter(X[:,2], X[:,0])  # we have picked weight as x axis and BP as y axis
plt.show()

# adding ones to the dataframe to act as the bias term after the plotting
df['ones'] =1
Y = df['X1']
X = df['X2', 'X3', 'ones']

""" we want to do three linear regression. one with x2 as input, second with x3 as input and third both as
input"""
X2only =df['X2','ones']
X3only =df['X3', 'ones']

"""since we will be plotting 3 graphs, let create a function for r-squared so that we will just be
calling it"""
def get_r2(X,Y):
    w = np.linalg.solve(np.dot(X.T,X),np.dot(X.T,Y))
    Yhat = np.dot(X,w)

    d1 = y - yhat
    d2 = y - y.mean()
    r2 = 1 -d1.dot(d1)/d2.dot(d2)
    return r2

print ("r2 for X2 only:", get_r2(X2only,Y))
print ("r2 for X3 only:", get_r2(X3only,Y))
print ("r2 for both:", get_r2( X,Y))

# note: noise improves our R value

