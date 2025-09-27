import Library
import numpy as np

matrix1=Library.read_matrix("gauss 1.txt")
matrix2=Library.read_matrix("gauss 2.txt")
L=Library.gauss(matrix1,matrix2)
print("Solution is ",L)

#Output=[-2.0, -2.0, 1.0]

matrix3=Library.read_matrix("gauss 3.txt")
matrix4=Library.read_matrix("gauss 4.txt")
Ls=Library.gauss(matrix3,matrix4)
print("Solution is ",Ls)

#Output is [-1.7618170439978598, 0.8962280338740136, 4.051931404116158, -1.6171308025395423, 2.0419135385019125, 0.1518324871559355]

