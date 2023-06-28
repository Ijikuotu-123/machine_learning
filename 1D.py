""" for a 1D sample, w  has one value and so is b """

import numpy as np   
import matplotlib.pyplot as plt # to visualize what we are doing

# for a simple linear regression, the equation is like this:
y = ax + b  # the y is y cap . the prediction y
# to load data. note we can also use np.read_csv()
x = []
y = []
for line in open('data_1d.csv'):
    x,y  = line.split(',')
    x.append(float(x))
    y.append(float(y))
    
# let's turn x and y into a numpy array
x = np.array(x)
y = np.array(y)

# plot to see what its looks like
plt.scatter(x, y)
plt.show()

# apply the equation we learned to calulate a and b
denominator = x.dot(x) - x.mean()* x.sum()
a = (y.dot(x) - y.mean()*x.sum())/denominator
b = (y.mean()*x.dot(x) - x.mean()*y.dot(x))/denominator

# calculate the predicted y
yhat = a*x + b

# plot it all
plt.scatter(x,y)
plt.plot(x,yhat) # to put a line across
plt.show()

#SECTION2
#Determing the effectivness of our model
# r2(r squared ) is used to determine how effective of model is
# r2 = 1 -SSres/SStot
# SSres(sum of square residual)= summation(yi - y(cap))squared
#SStot(Sum of square total)=summation(yi -y(mean))squared

# to calculate r2
d1 = y -yhat
d2 = y - y.mean()
r2 = 1 -d1.dot(d1)/d2.dot(d2)
print(r2)















