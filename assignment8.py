import Library
import math

def f(x,y,z):
    f1=x**2 + y -37
    f2=x-y**2 -5
    f3=x+y+z - 3
    return [f1,f2,f3]
def f_(x,y,z):
    x_1,y_1,z_1=2*x ,1,0
    x_2,y_2,z_2=1,-2*y ,0
    x_3,y_3,z_3=1,1,1  
    return ([[x_1,y_1,z_1],[x_2,y_2,z_2],[x_3,y_3,z_3]] )
x,y,z=3,0.99,-2
L=[x,y,z]
print(Library.MultiNewton(f,f_,L,x,y,z))

# Output ([5.9999999997054605, 1.0000000035863266, -4.000000003291787], 6) .Solution converges after 6 iterations
"""def Multi_in(f,f_,L,x,y,z):
    E=f(x,y,z)
    E_=f_(x,y,z)
    iv=Library.inverse(E_)
    for k in range(len(E)):
     s=0
     for l in range(len(E)):
      s=s+(iv[k][l]*E[l])
     L[k]=L[k]-s 
    return L
x,y,z=3,0.99,-2
L=[x,y,z]
print(Library.MultiNewton(f,f_,L,x,y,z))
L=[x,y,z]
Xi=L.copy()
print(Xi)
X_=Multi_in(f,f_,L,x,y,z)   
c=0 
while math.sqrt((X_[0]-Xi[0])**2 + (X_[1]-Xi[1])**2 + (X_[2]-Xi[2])**2 )>10**-6:
  x,y,z=X_[0],X_[1],X_[2]
  Xi=X_.copy()
  X_=Multi_in(f,f_,X_,x,y,z)
  c=c+1
print(Xi,c)"""

#Using Fixed point method
def values(x,y,z):
   y=math.sqrt(x-5)
   x=math.sqrt(37-y)
   z=3-x-y
   return x,y,z #initial values
x,y,z=10,4,-2
xi,yi,zi,c=Library.Multi_Fixed(values,x,y,z)
print("no. of ieration",c)  
print("values are",xi,yi,zi)

#no. of ieration 6
#values are 5.999999999442171 1.0000000066939552 -4.000000006136126