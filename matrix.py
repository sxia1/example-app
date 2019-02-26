"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    print(" ".join(str(i) for i in matrix[0]))
    print(" ".join(str(i) for i in matrix[1]))
    print(" ".join(str(i) for i in matrix[2]))
    print(" ".join(str(i) for i in matrix[3]))
    print()

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if (row == col):
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for i in range(len(m2[0])):
        m2[0][i] = m1[0][0]*m2[0][i] + m1[0][1]*m2[1][i] + m1[0][2]*m2[2][i] + m1[0][3]*m2[3][i]
        m2[1][i] = m1[1][0]*m2[0][i] + m1[1][1]*m2[1][i] + m1[1][2]*m2[2][i] + m1[1][3]*m2[3][i]
        m2[2][i] = m1[2][0]*m2[0][i] + m1[2][1]*m2[1][i] + m1[2][2]*m2[2][i] + m1[2][3]*m2[3][i]
        m2[3][i] = m1[3][0]*m2[0][i] + m1[3][1]*m2[1][i] + m1[3][2]*m2[2][i] + m1[3][3]*m2[3][i]

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
