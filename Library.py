import numpy as np
import math

def read_matrix(filename) :
    with open(filename , "r" ) as f :
        matrix = [ ]
        for line in f :
            # S p l i t t h e l i n e i n t o numbers and c o n v e r t t o i n t / f l o a t
            row = [float(num) for num in line.strip( ).split( )]
            matrix.append ( row )
    return matrix

#plot between 0 to 1

def lcg2(a,c,m,x_0,n):
    L=[x_0]
    for k in range(0,n):
        x_=(a*x_0 +c)%m
        x_0=x_
        L.append(x_0/m)
    return L


def gauss(A,B):
#augmenting the matrix1
 for r in range(len(B[0])):
  for k in range(len(A)):
    A[k].append(B[k][r])

 #swapping
 c=0
 g=A
 p=g[0][0]
 for k in range(len(A)):
        if abs(g[k][0])>p:
            p=g[k][0]
            c=k
        
 q=A[0]        
 A[0]=A[c]
 A[c]=q

 print(A)
 #Normalising the pivot row  
 for e in range(len(A)):    
  
    L=[]
    for k in range(len(A[0])):
         L.append(A[e][k]/A[e][e])
    A[e]=L
    #multiply
    for k in range(len(A)):
        
        if k!=e:
             L1 = []
             for s in range(len(A[0])):
                o=A[e][s]*A[k][e]
                L1.append(A[k][s]-o)
             A[k]=L1 
 #printing last column of A            
 Lw=[]
 for k in range(len(A)):
    Lw.append(A[k][-1])
 return Lw              

#inverse of matrix using Gauss Jordon
def inverse(A):
 L=[]
 L_=[]
 for g in range(len(A)):
    for c in range(len(A)):
        if g==c:
            L_.append(1)
        else:
            L_.append(0)
    L.append(L_)
    L_=[]
 Lsol=gauss(A,L)
    


 Lk=[]
 Lk_=[]   
 for j in range(len(Lsol)):
    for p in range(len(Lsol)):
       Lk_.append(Lsol[p][j])
    Lk.append(Lk_)
    Lk_=[]

 return Lk    


#final matrix is L_ and U_
def LU_decomposition(matrixa,L_,U_):
  for i in range(len(matrixa)):
      for j in range(len(matrixa)):
           if i>j:
                t=0
                l=0
                for k in range(0,j):
                  c=L_[i][k]*U_[k][j] +t
                  t=c
                L_[i][j]=(matrixa[i][j]-t)  / U_[j][j]
                
                for w in range(0,i):
                  g=L_[i][w]*U_[w][j]+l
                  l=g
                U_[i][j]=matrixa[i][j]-l
                

           if i<=j:
                y=0
                for s in range(0,i):     
                  e=L_[i][s]*U_[s][j]+y
                  y=e
                U_[i][j]=matrixa[i][j]-y
  return L_,U_    

#LU decomposition using forward and backward substitution
          
def LU(matrixA,matrixB,A,B):
  X=[]
  X_=[]
  Y=[]
  Y_=[]
  for k in range(len(matrixA)):
        for t in range(1):
           X.append(0)
           Y.append(0)
        X_.append(X)
        Y_.append(Y)
        Y=[]
        X=[]

#forward substitution

  for i in range(len(matrixA)):
      c=0
      for j in range(0,i):
            t=A[i][j]*Y_[j][0] +c
            c=t
      Y_[i][0]=(matrixB[i][0] -c)/A[i][i]


#backward substitution
  for i in range(len(matrixA)-1,-1,-1):
      t=0
      for j in range(i+1,len(matrixA)):
        v=B[i][j]*X_[j][0]+t
        t=v
      X_[i][0]=(Y_[i][0]-t)/B[i][i]
  return X_



def ch(matrix):
 L_=[]
 for k in range(len(matrix)):
     L=[]
     for p in range(len(matrix)):
         L.append(0)
     L_.append(L)

 for i in range(len(L_)):
     for j in range(len(L_)):        
         if i==j:
             f=0
             for g in range(0,i):
                 q=(L_[i][g])**2+f
                 f=q
             L_[i][i]=np.sqrt(matrix[i][i]-f)

         if i<j:
             c=0
             for k in range(0,i):
                 t=L_[i][k]*L_[k][j] +c
                 c=t
             L_[i][j]=(matrix[i][j] - c )/ L_[i][i]     

   


 Lt_=[]
 for k in range(len(matrix)):
     Lt=[]
     for p in range(len(matrix)):
         Lt.append(0)
     Lt_.append(Lt)


 for c in range(len(Lt_)):
    for z in range(len(Lt_)):
        Lt_[z][c]=L_[c][z]
 return L_,Lt_          

def Jac(A,B):
 c=0
 L=[]
 for k in range(len(A)):
    L.append(0)
 L__=[]
 def list(L):
  c=0
  L_=[]
  for i in range(len(A)):
    for j in range(len(A)):
        if j!=i:
            t=A[i][j]*L[j] +c
            c=t
    x=(B[i][0]-c)    /A[i][i]  
    L_.append(x)
    c=0
  return L_
  
 for l in range(20):
   L__.append(list(L))
   L=L__[l]




 for v in range(len(L__)):
     if v==len(L__)-1:
        break
     j=0
     for p in range(len(A)):
        h=(L__[v+1][p]-L__[v][p])**2 +j
        j=h
        
         
     if math.sqrt(j)<10**-6:
        break  
 return L__[v]   
        

def Seidel(A,B):
 L=[]
 for k in range(len(A)):
  L.append(0)




 def matrix(L):
  w=0
  s=0
  p=0
  for i in range(len(A)):
    if i>=1:
      p=0
      s=0
      for j in range(0,i):
        c=A[i][j]*L[j] +s
        s=c
      for r in range(i+1,len(A)):
        b=A[i][r]*L[r]+ p
        p=b
      L[i]=(B[i][0]-s-p)/A[i][i]  


    else:
      w=0
      for k in range(i+1,len(A)):
        d=A[i][k]*L[k]+w    
        w=d
      L[i]=(B[i][0] - w) / A[i][i] 
  
  return L    

 L__=[]
 for l in range(40):
   L__.append(matrix(L))
   L=L__[l]




 for v in range(len(L__)):
     if v==len(L__)-1:
        break
     j=0
     for p in range(len(A)):
        h=(L__[v+1][p]-L__[v][p])**2 +j
        j=h
        
         
     if math.sqrt(j)<10**-6:
        break  
 return L__[v]   
  






    

            

 


  
       









    

