'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       February 6 2019
written for:        Homework4 Task9
course:             Math 5610

purpose:            Implement a method that will generate a diagonally dominant matrix that has real values in all entries of the matrix.
'''
import random

import sys, os
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import vector_1norm

def gen_diagdom_sym_matrix(width=5):
    A = [[0 for i in range(width)] for j in range(width)]
    for i in range(0, width):
        for j in range(i, width):
            value = random.random()
            A[j][i] = value
            A[i][j] = value
    for i in range(0, width):
        A[i][i] += width
    return A

#The code below is used just for testing.
#A_ = gen_diagdom_sym_matrix()
#for i in range(len(A_)):
#    print(A_[i])


