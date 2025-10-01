#First checking if the function is bracketed
import numpy as np
import Library

a=1.5
b=3

def f(x):
    y=np.log(x/2)-np.sin((5*x)/2)
    return y
print(Library.bracket(a,b,f,0.1))
#the function is already bracketed
print(Library.Bisection(a,b,f))
#(2.6231406927108765, 22)

def f(x):
    y=np.log(x/2)-np.sin((5*x)/2)
    return y
print(Library.Falsi(a,b,f))

#Output by Regula Falsi method with no. of iterations
#(2.6231403354363083, 9)

#Question2 
# k is beta here
import numpy as np
def f(x):
    y=-x-np.cos(x)
    return y
print(Library.bracket(2,4,f,0.1))
#f(a) and f(b) are 0.8134913038547624 -3.346356379136388
#number of iteration 10