#using Doolittle method
#importing L and U from Lulibrary

import Library

matrix=Library.read_matrix("LU1.txt")
S=Library.LU_decomposition(matrix)
L=[]
U=[]
L_=[]
U_=[]
for k in range(len(S)):
      for g in range(len(S)):
            if k>g:
             L.append(S[k][g])
             U.append(0)
            elif k<g:
                 U.append(S[k][g])
                 L.append(0)
            else:
                 L.append(1)
                 U.append(S[k][g])
      L_.append(L)
      U_.append(U)
      L=[]
      U=[]
print("L is",L_)
print("U is",U_)


#Output=
#S is [[1, 2, 4], [3.0, 2.0, 2.0], [2.0, 1.0, 3.0]]
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