import numpy as np
import matplotlib.pyplot as plt
import Library
# t is x and T
# v is z 
#t is x


def f(v):
    return v
def f_(x,v):
    return -( 0.01*(20 -x) )


L=[]
L_=[]
Lnew=[]
T=[]
V=[]
h=0.1
t=0
v1=10
x=40
L.append(x)
T.append(t)
V.append(v1)
l,V,T=Library.newRange_kutta(h,x,v1,f,f_,t,L,10,T,V)
g1=l[-1]


T=[]
V=[]
v2=20
L_.append(x)
T.append(t)
V.append(v2)
l_,V,T=Library.newRange_kutta(h,x,v2,f,f_,t,L_,10,T,V)
g2=l_[-1]



T=[]
V=[]
Lnew.append(x)
T.append(t)
newv=v1+(((v2-v1)/(g2-g1))*(200-g1) )
V.append(newv)
lnew,V,T=Library.newRange_kutta(h,x,newv,f,f_,t,Lnew,10,T,V)


plt.plot(T,l,label="initial guess (z=10)")
plt.plot(T,l_,label="final guess(z=20)")
plt.plot(T,lnew,label="After interpolation")
plt.legend()
plt.show()

for k in range(len(lnew)):
   if 100-0.35<=lnew[k]<=100+0.35:
      
      break
   else:
   
      t=t+h

print("The value of x at which temperature is 100 is ",t)
#Output is x=4.5


#question2
#nx,nt=number of position grid and number of time grid
#L contains the values of temperature at different time steps(nt)
def parameters(nx,nt): 

 hx=2/nx
 ht=4/nt
 alpha=ht/(hx**2)  
 if alpha<=0.5 :
  L=[]
  V=[]
  x=0
  L.append(0)
  while x<=2:
   x=x+hx
   L.append(x)
 
  for i in range(len(L)):
   if 1- (2/(2*nx))<L[i]<1+(2/(2*nx)):
     p=L[i]
     V.append(300)
   else:
      V.append(0)

  A=Library.Shooting_method(V,alpha)
  return V,A,L

V,A,L=parameters(10,5000) #nx is 10 and nt is 5000
T_=[0,10,20,50,100,200,500,5000]
for t in T_:
 Y=Library.shootingplot(t,V,A)

 plt.plot(L,Y,label="plot at different temperatures")
plt.xlabel("position")
plt.ylabel("temperature(C)")
plt.show()
