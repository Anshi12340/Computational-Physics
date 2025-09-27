#A is L
#B is U
#Using Doolittle method

import Library
matrixA=Library.read_matrix("gauss 3.txt")
matrixB=Library.read_matrix("gauss 4.txt")


#making L and U
L_=[]
U_=[]
for k in range(len(matrixA)):
     L=[]
     U=[]
     for p in range(len(matrixA)):
          if k==p:
               L.append(1)
               U.append(0)
          if k<p or k>p:
               U.append(0)
               L.append(0)        
     L_.append(L)
     U_.append(U)
       

A,B=Library.LU_decomposition(matrixA,L_,U_)
X=Library.LU(matrixA,matrixB,A,B)
print("Solutions is ",X)

#Output=[[-1.761817043997862], [0.8962280338740133], [4.051931404116158], [-1.6171308025395421], [2.041913538501913], [0.15183248715593525]]