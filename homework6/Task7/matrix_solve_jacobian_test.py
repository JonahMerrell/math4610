import random
import sys, os
import time
sys.path.append(os.path.abspath('../../mylibrary'))
from _mymodules import gen_rand_matrix,gen_sym_matrix,gen_diagdom_matrix,gen_diagdom_sym_matrix ,matrix_mult, convert_vec_mat, matrix_solve_jacobian

def matrix_solve_jacobian_test():
    matrix1 = gen_rand_matrix(100,100)
    matrix2 = gen_sym_matrix(100)
    matrix3 = gen_diagdom_matrix(100)
    matrix4 = gen_diagdom_sym_matrix(100)
    matrices = [matrix1,matrix2,matrix3,matrix4]
    vector = [1] * len(matrix1)
    for i in range(len(matrices)):
        b = matrix_mult(matrices[i],convert_vec_mat(vector))
        starttime = time.time()
        solution = matrix_solve_jacobian(matrices[i], convert_vec_mat(b), 0.00001, 1000,getIterCount=True)
        print("Time: " + str(time.time() - starttime))
        print("# of iterations: " + str(solution[1]))
        print(solution[0])

matrix_solve_jacobian_test()
