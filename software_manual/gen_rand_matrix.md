# Software Manual (gen_rand_matrix.py)

## [Back](softwaremanual.md)

**Routine Name:**           gen_rand_matrix.py

**Author:** Jonah Merrell

**Language:** Python 3.7.0

**Description/Purpose:** This routine will create a n*n matrix (the size is inputted from the user)
 with random entries from 0 to 1.

**Input:** argument1: The width of the matrix

**Output:** This routine returns the n*n matrix.

**Usage/Example:**

Below shows an example of generating a matrix using the routine "gen_rand_matrix". Then the matrix is printed 
one row at a time (for readability's sake). 

      A_ = gen_rand_matrix(4)
      for i in range(len(A_)):
          print(A_[i])


Output from the lines above:

      [0.18361695228266373, 0.24419516412171816, 0.6462210640959352, 0.37810880655946166]
      [0.06450890123439323, 0.8157962192772203, 0.4892644472021095, 0.7642990862352379]
      [0.9004559438860636, 0.21503714922621286, 0.26971632524829736, 0.6306694825635641]
      [0.6187029394329355, 0.8773015910518385, 0.31064448692689783, 0.22036563737472858]

In the example above, "4" was chosen to be the width of the matrix.
 The above matrix generated is just one possible matrix generated, since the content of the matrix is generated randomly.
 Calling this function again would (likely) produce a matrix with different randomly generated numbers inside.

**Implementation/Code:** The following is the code for gen_rand_matrix()


      import random
      
      def gen_rand_matrix(width=5):
          A = [[0 for i in range(width)] for j in range(width)]
          for i in range(0,width):
              for j in range(0, width):
                  A[j][i] = random.random()
          return A
