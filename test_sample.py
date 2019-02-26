from matrix import *
from draw import *

matrix = new_matrix()

A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
B = [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]



def test_add_edge():
    add_edge(matrix, 1, 1, 1, 1, 1, 1)
    add_edge(matrix, 1, 1, 1, 1, 1, 1)
    assert matrix == [[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1],[0,0,0,0,1,1,1,1]]

def test_ident():
    ident(matrix)
    assert matrix == [[1,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,1,0,1,1,1,1],[0,0,0,1,1,1,1,1]]

def test_mult():
    matrix_mult(matrix, A)
    assert A == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    ident(matrix)
    matrix_mult(matrix, B)
    assert B == [[11,12,13,14],[15,16,17,18],[19,20,21,22],[23,24,25,26]]
    
