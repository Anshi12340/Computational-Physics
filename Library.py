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
 """Lw=[]
 for k in range(len(A)):
    Lw.append(A[k][-1])
 print(Lw)   
 return Lw    """          
 Lw_=[]
 Lw=[]
 for d in range(len(A),len(A[0])):
  
  for k in range(len(A)):
    Lw_.append(A[k][d])
  
  Lw.append(Lw_)
  Lw_=[]  
 
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
     for j in range(i,len(L_)):        
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
             L_[j][i] = L_[i][j]
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
    x=(B[i][0]-c)/A[i][i]  
    L_.append(x)
    c=0
  return L_
  
 while True:
   Li=L.copy()
   L=list(L)
   sum=0
   for k in range(len(L)):
     sum=sum+((L[k]-Li[k])**2)
   if math.sqrt(sum)<10**-6:
     break  
    
 return L 
 
        

def Seidel(A,B):
 import math
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

 while True:
   Li=L.copy()
   L=matrix(L)
   sum=0
   for k in range(len(L)):
     sum=sum+((L[k]-Li[k])**2)
   if math.sqrt(sum)<10**-6:
     break  
    
 return L

def bracket(a,b,f,k): #k is initial guess #c for counting
 c=0
 if f(a)*f(b)<0:
    print("already bracketed")   
 while f(a)*f(b)>0:
  if np.abs(f(a))<np.abs(f(b)):
     a=a-k*(b-a)
     c=c+1
  elif np.abs(f(a))>np.abs(f(b)):
     b=b+k*(b-a)
     c=c+1
 return a,b,c 

def Falsi(a,b,f):
  if f(a)*f(b)<0:
   count=0
   while True:
    c=b-(((b-a)*f(b))/(f(b)-f(a)))
    if np.abs(b-a)<10**-6 or np.abs(f(c))<10**-6:
      return c,count
    else:
     if f(a)*f(c)<0:
          b=c
          count=count+1  
     else:
           a=c
           count=count+1
  else:
     print("bracketing not done")

 

def Bisection(a,b,f):
  count=0
  if f(a)*f(b)<0:
   while True:
     c=(a+b)/2
     if np.abs(b-a)<10**-6 or np.abs(f(c))<10**-6:
        return c,count
     else:
    
        if f(a)*f(c)<0:
           b=c
           count=count+1
        else:
           a=c
           count=count+1  
  else:
     print("bracketing not done")          
  
def Raphson(f,f_,x_): #f and f_ are function and derivative of function and x_ is initial guess
  c=0
  while True:
    x=x_ - f(x_)/f_(x_)
    if np.abs(x-x_)<10**-6 and f(x)<10**-6:
       return x,f(x),c  
    else:
        x_=x
        c=c+1
       

#Multivariable        
def MultiNewton(f,f_,L,x,y,z):
  def Multi_in(f,f_,L,x,y,z):
     E=f(x,y,z)
     E_=f_(x,y,z)
     iv=inverse(E_)
     for k in range(len(E)):
      s=0
      for l in range(len(E)):
       s=s+(iv[k][l]*E[l])
      L[k]=L[k]-s 
     return L
  X_=Multi_in(f,f_,L,x,y,z) 
  Xi=L.copy()
  X_=Multi_in(f,f_,L,x,y,z)   
  c=0 
  while math.sqrt((X_[0]-Xi[0])**2 + (X_[1]-Xi[1])**2 + (X_[2]-Xi[2])**2 )>10**-6:
    x,y,z=X_[0],X_[1],X_[2]
    Xi=X_.copy()
    X_=Multi_in(f,f_,X_,x,y,z)
    c=c+1
  return(Xi,c)

def Multi_Fixed(values,x,y,z):#values is name of a function and requires 4 input values
 xi,yi,zi=values(x,y,z)
 c=0
 while math.sqrt((xi-x)**2 + (yi-y)**2 + (zi-z)**2 )>10**-6:
  x,y,z=xi,yi,zi
  xi,yi,zi=values(x,y,z)
  c=c+1
 return xi,yi,zi,c

def Laguerre(L,x): #entries ofL must be in decreasing powers of x
 epsilon=10**-6
 def co(L,x):
    sum=0
    for k in range(len(L)):
      sum=sum+L[k]*x**(-k-1+len(L)) 
    
    return sum
 def der(L,x):
   s_=0
   for v in range(len(L)):
      if (len(L)-v-2)>=0:                               #-1x2+4x -4
       s_=s_+ L[v]*(len(L)-1-v)*x**(len(L)-v-2)         #-2x+4
  
   return s_
 def dder(L,x):
   s__=0
   for w in range(len(L)):
    if (len(L)-w-3)>=0:
     s__= s__+ L[w]*(len(L)-w-1)*(-w+len(L)-2)*x** (len(L)-w-3) #x**3+x**2+x +1
  
   return s__ 
 def deflation(L,x):  
   if co(L,x) !=0:
     g=der(L,x)/co(L,x)
     h=g**2 - (dder(L,x)/co(L,x))
     n=len(L)-1                                                              
     a1=  n/(g+(np.sqrt((n-1)*(n*h-(g**2)))))                        
     a2= n/(g-(np.sqrt((n-1)*(n*h-(g**2))))) 
     if np.abs(a1)<np.abs(a2):
       a=a1
     else:
       a=a2
   else:
      root=x
      return root
   xnew=x-a 
   while np.abs(xnew-x)>epsilon:
     x=xnew
    
     xnew=deflation(L,x)
   root=x
   
   return root
  
 def synthetic_division(L,value): 
  Lnew=[]
  Lnew.append(L[0])
  for l in range(len(L)):
   if l+1<len(L):
    Lnew.append(value*Lnew[l]+L[l+1])
  
  return Lnew
 roots=[]
 for t in range(len(L)-1):
  
  value=deflation(L,x)
  L_=synthetic_division(L,value)
  roots.append(value)
  L=L_[0:len(L)-1]
  x=value
 return roots
  
def Midpoint(a,b,N,h,f):
 sum=0
 x=a
 for k in range(N):
    x=x+(k*h)
    if x<=b:
     mid=((x)+(x+h))/2
     
     sum=sum+(f(mid))
     
    x=a
 return sum *h   


def Trapezoid(a,b,N,h,f):
  sum=0
  x=a
  for k in range(N):
    x=x+(k*h)
    if x<=b:
     sum=sum+((f(x)+f(x+h)))
     x=a+h
    x=a 
  return sum *(h/2)  