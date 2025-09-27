#using Doolittle method
#importing L and U from Lulibrary

import Library

matrix=Library.read_matrix("LU1.txt")

#making L and U
L_=[]
U_=[]
for k in range(len(matrix)):
     L=[]
     U=[]
     for p in range(len(matrix)):
          if k==p:
               L.append(1)
               U.append(0)
          if k<p or k>p:
               U.append(0)
               L.append(0)        
     L_.append(L)
     U_.append(U)
       

L,U=Library.LU_decomposition(matrix,L_,U_)
print("L is",L)
print("U is",U)

#Output=
#L is [[1, 0, 0], [3.0, 1, 0], [2.0, 1.0, 1]]
#U is [[1.0, 2.0, 4.0], [0.0, 2.0, 2.0], [0.0, 0.0, 3.0]]

#Verification by multiplying L and U matrix
A=[]
L=[]
for p in range(len(matrix)):
      for q in range(len(matrix)):
            x=0
            for r in range(len(matrix)):
                  c=L_[p][r]*U_[r][q]+x
                  x=c
            L.append(x)
      A.append(L)
      L=[]
print("Matrix obtained after multiplication of L with U",A)
print("Original matrix",matrix)

#A=[[1.0, 2.0, 4.0], [3.0, 8.0, 14.0], [2.0, 6.0, 13.0]]
#matrix=[[1.0, 2.0, 4.0], [3.0, 8.0, 14.0], [2.0, 6.0, 13.0]]

#Both matrices are same