import matplotlib.pyplot as plt
import numpy as np
import Library

def derivative(x,y):
   return (x+y)**2
   
h=0.1
X=[]
Y=[]
Y_=[]
y=1
x=0
X.append(x)
Y.append(y)
while x<=(np.pi/5):
  y,x=Library.Range_Kutta(h,x,y,derivative)
  X.append(x)
  Y.append(y)
print("y values by Range Kutta method",Y)



def mainf(x):
   return np.tan(x+ ((np.pi)/4)) -x 
for k in X:
   Y_.append(mainf(k))



#step size= 0.25
h=0.25
X2=[]
Y2=[]

y=1
x=0
X2.append(x)
Y2.append(y)
while x<=(np.pi/5):
  y,x=Library.Range_Kutta(h,x,y,derivative)
  X2.append(x)
  Y2.append(y)
print("y values by Range Kutta method",Y2)

#step size=0.45
h=0.45
X3=[]
Y3=[]
y=1
x=0
X3.append(x)
Y3.append(y)
while x<=(np.pi/5):
  y,x=Library.Range_Kutta(h,x,y,derivative)
  X3.append(x)
  Y3.append(y)
print("y values by Range Kutta method",Y3)

plt.plot(X,Y,label="Y values by numerical method of step size 0.1",marker="o")
plt.plot(X2,Y2,label="Y values by numerical method of step size 0.25",marker="*")
plt.plot(X3,Y3,label="Y values by numerical method of step size 0.45",marker="*")
plt.plot(X,Y_,label="from Analytic method",color="black")
plt.legend()
plt.show()

#y values of step size 0.1 [1, 1.1230489138367843, 1.308496167191276, 1.5957541602334353, 2.0648996869578835, 2.907820425151802, 4.7278968165905155, 10.853932075720177]
# step size 0.25 [1, 1.43555804125693, 2.8972272051287176, 17.885430277813693]
#step size 0.45 [1, 2.3890595350788653, 109.96022593101979]

#question2
"""
X=[]
V=[]
T=[]
E=[]
def newRange_Kutta(h,x,v,a,f,t):


    xi=x
    v0=v
    a0=a
    k1x=h*v0
    k1v=h*a0

    v,x,t=v0+k1v/2,xi+k1x/2,t+(h/2)
    
    k2x=h*(v0+k1v/2)
    k2v=h*f(x,v)
    v,x,t=v0+k2v/2,xi+k2x/2,t+(h/2)
    k3x=h*(v0+k2v/2)
    k3v=h*f(x,v)

    v,x,t=v0+k3v,xi+k3x,t+h
    k4x=h*(v0+k3v)
    k4v=h*f(x,v)

    x=xi+ ((k1x+2*k2x + 2*k3x +k4x)/6)
    v=v0+ ((k1v+2*k2v + 2*k3v +k4v)/6)
    return x,v,t
u=0.15
w=1
m=1
def f(x,v):
   a= - u *v  - ((w)**2 )*x
   return a
v=0
t=0
x=1
a=-1
X.append(x)
V.append(v)
T.append(t)
E.append(0.5*(x**2) +( 0.5 *(v**2)))
while t<=40:
   
  x,v,t=newRange_Kutta(0.1,x,v,a,f,t)
  E.append(0.5*(x**2) +( 0.5 *(v**2)))
  X.append(x)
  V.append(v)
  T.append(t)
plt.plot(X,V,label="plot of x and v")
plt.legend()
plt.show()
plt.plot(T,E,label="plot of E and t")
plt.legend()
plt.show()
"""


L=[]
E=[]
T=[]
V=[]
u=0.15
w=1
m=1
v=0
t=0
x=1
a=-1
L.append(x)
V.append(v)
T.append(t)


def f(v):
    return v

def f_(x,v):
    a= - u *v  - ((w)**2 )*x
    return a
L,V,T=Library.newRange_kutta(0.1,x,v,f,f_,t,L,40,T,V)
for k in range(len(L)):
   E.append((0.5*(L[k]**2)) + (0.5*(V[k]**2)))


plt.plot(T,E,label="Energy v/s time curve")
plt.xlabel("time")
plt.ylabel("energy")
plt.legend()
plt.show()
plt.plot(L,V,label="x v/s v curve")
plt.xlabel("position")
plt.ylabel("velocity")
plt.legend()
plt.show()
plt.plot(T,L,label="x v/s t curve")
plt.xlabel("time")
plt.ylabel("position")
plt.legend()
plt.show()
plt.plot(T,V,label="v v/s t curve")
plt.xlabel("time")
plt.ylabel("velocity")
plt.legend()
plt.show()
