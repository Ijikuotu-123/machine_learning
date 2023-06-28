import numpy as np   
import matplotlib.pyplot as plt # to visualize what we are doing
import re   # helps in removing things we don't want in our csv

X =[]
Y=[]

non_decimal = re.compile(r'[^\d] + ')    # remove non_decimal from the input
for line in open('moore.csv'):
    r = line.split('\t')  # split the line by tab
    x=int(non_decimal.sub('',r[2].split('[')[0]))  # r[2] because x is in column 2.
    y=int(non_decimal.sub('',r[1].split('[')[0]))
    X.append(x)
    Y.append(y)

X = np.array(X)
Y = np.array(Y)

plt.scatter(X, Y)
plt.show()

Y = np.log(Y)
plt.scatter(X, Y)
plt.show()

denominator = x.dot(x) - x.mean()* x.sum()
a = (y.dot(x) - y.mean()*x.sum())/denominator
b = (y.mean()*x.dot(x) - x.mean()*y.dot(x))/denominator

yhat = a*x + b

plt.scatter(x,y)
plt.plot(x,yhat)
plt.show()

d1 = y -yhat
d2 = y - y.mean()
r2 = 1 -d1.dot(d1)/d2.dot(d2)
print("a:", a, "b:",b)
print(r2)

# r2 that is negative shows that the model is bad.




