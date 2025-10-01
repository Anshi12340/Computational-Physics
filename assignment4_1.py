#matrix is A
#matrixs is b 
#At is L
#A is U
import Library
import numpy as np
matrix=Library.read_matrix("Cholesky.txt")
matrixs=Library.read_matrix("Cholesky_.txt")

A=Library.ch(matrix)
At =A
print(A,At)
X=Library.LU(matrix,matrixs,At,A)
print("Solutions by Cholesky method",X)

#Output=[[0.0], [1.0], [1.0], [1.0000000000000002]]

Xs=Library.Jac(matrix,matrixs)
print("By Jacobi method",Xs)

#Outpu is [0.0, 0.9987793010095429, 0.9993896422356856, 0.9993896422356856]
