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
#(2.623140335083008, 17)

def f(x):
    y=np.log(x/2)-np.sin((5*x)/2)
    return y
print(Library.Falsi(a,b,f))

#Output by Regula Falsi method with no. of iterations
#(2.62314050689124, 4)

#Question2 
# k is beta here
#0.1 is initial guess
import numpy as np
def f(x):
    y=-x-np.cos(x)
    return y
d,e,i=Library.bracket(2,4,f,0.1)
print(d,e,i)
print(f(d),f(e))
#interval is -1.1874849202000002 4 
#f(a) and f(b) are 0.8134913038547624 -3.346356379136388
#number of iteration 10