'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       September 13 2019
written for:        Homework2 Task3
course:             Math 4610

purpose:            Write code that implements fixed point iteration

'''
import math

#def function(x):
#    return x  * math.cosh(x)+ pow(x,3) - math.pi
#    return (math.pi-pow(x,3))/math.cosh(x) - x
#    return x - (pow(x,3) - math.pi) / math.cosh(x)

def root_solve_fixed_point(function, x_0, tol, maxiter):

    error = 10* tol
    x = x_0
    iter = 0
    while (error > tol and iter < maxiter):
        x = x + function(x)
        error = abs(x - x_0)
        x_0 = x
        iter +=1
    return x




#The code below is used just for testing.
#def function(x):
#    return math.cos(x) - x
#print(root_solve_fixed_point(function, 0.9, 0.0001, 50))




