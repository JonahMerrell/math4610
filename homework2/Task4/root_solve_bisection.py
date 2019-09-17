'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       September 17 2019
written for:        Homework2 Task4
course:             Math 4610

purpose:            Write code that implements bisection iteration

'''
import math

def root_solve_bisection(function, a, b, tol):
    #Check to see if a or b are already the solution
    if (function(a) == 0) :
        return a
    if (function(b) == 0) :
        return b
    #Calculate the max iterations needed for this method
    maxiter = math.ceil(-math.log2(tol/(b-a)) + 1)
    val = function(a)*function(b)
    if (val >= 0):
        return "a and b are not valid for this iteration technique"
    c = 0
    for i in range(maxiter):
        c = 0.5 * (a + b)
        if (function(c) == 0):
            return
        if (function(a)*function(c) < 0):
            b = c
        else:
            a = c
    return c




#The code below is used just for testing.
def function(x):
    return math.cos(x) - x
print(root_solve_bisection(function, 0, 1, 0.000001))





