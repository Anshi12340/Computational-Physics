import numpy as np
import Library

def f(x):
    y=3*x + np.sin(x) -np.exp(x)
    return y
def f_(x):
    y_=3 +np.cos(x) - np.exp(x)
    return y_
x=1 #initial guess
s,s_,c=Library.Raphson(f,f_,x)
print("root is ",s)
print("function is",s_)
print("numbers of iterations",c)

#Output is 
#root is  0.36042170296019965
#function is -3.11972669919669e-13
#numbers of iterations 4

#bisection method

x,count=Library.Bisection(-1.5,1.5,f)
print("root is",x)
print("iterations",count)
#root is 0.3604220151901245
#iterations 23

#Falsi Method

v,vcount=Library.Falsi(-1.5,1.5,f)
print("root is",v)
print("iterations",vcount)

#Result is both Newton Method is taking 4 iterations whereas Bisection and Falsi method are taking 23 and 23 iterations

#Question 2
#fixed point method

#it can take more steps
import numpy as np
x_=2.7
n=0 #count
for k in range(100000):

  x=(x_**2 - 3)/2
  if np.abs(x-x_)<10**-6:
    break
  else:
    x_=x
    n=n+1
print("root is =",x)
print("number of steps to converge=",n)  

#root is = -0.9955242875343852
#number of steps to converge= 100000
#--- (later)