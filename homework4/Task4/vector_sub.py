'''
coding language:    Python 3.7.0

written by:         Jonah Merrell
date written:       October 29 2019
written for:        Homework4 Task4
course:             Math 4610

purpose:            Add the components of 2 equal size vectors together.
'''



def vector_sub(vector1,vector2):
    vector_sum = [0]* len(vector1)
    for i in range(len(vector_sum)):
        vector_sum[i] = vector1[i] - vector2[i]

    return vector_sum


#The code below is used just for testing.
vector1 = [5,7,9,2,5]
vector2 = [8,2,3,6,9]
print(vector_sub(vector1,vector2))

