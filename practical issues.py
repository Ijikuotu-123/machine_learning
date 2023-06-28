# WHAT DOES ALL THESE LETTERS MEAN

# DATA
# Data come in pairs: input and output
# Goal: predict output given an input
# output is also called target
# Typically we use X for input and Y for output/target. somestimes we use T for target

# SHAPE
#  X is an N X D matrix
# N = number of samples(rows)
# D = number of features (columns)
# Y is an N-length vector. can be thought of as Nx1 column vector(but need to be careful in code)
# y-hat (predictions) is the same size as Y

# ERROR/COST
# Error = Cost
# letter E or C is used to represent them
# in every situation we would like to minimize error/cost

# OBJECTIVE 
# Objective may be used in place of error or cost. it is a more genral term so we need to specify whether we 
# want to maximize it or mininmize it.
# note: minimizing E is the same as maximizing -E
# it represented with the letter j

# L2 REGULARIZATION
# L2 regularization is a way of reducing the complexity of the model and prevent overfitting to outliers
#  w= (λI + X^TX)^-1 X^TY    I is identity matrix
# L2 REGULARIZATION CODE

import numpy as np