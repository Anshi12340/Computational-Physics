import numpy as np
import Library
import matplotlib.pyplot as plt
def f(x):
    return (1/x)
a=1
b=2

N=((((b-a)**5 ) * 24 )/(180*(10**-6)) )**(1/4)
print("N for Simpson",N)
N1=( (((b-a)**3) *2)/(24*(10**-6))) **(1/2)
print("N for Mid point",N1)

print(Library.Simpson(a,b,20,(1/20),f))
print(Library.Midpoint(a,b,288,1/288,f))
#N for Simpson 19.108855844087337
#for Mid point 288.67513459481285
# For Simpson  integral value is 0.6591730156907568 
# For mid point integral value is  0.6931468038007155

# 2nd Function
def f_1(x):
    return x*np.cos(x)
a1=0
b1=3.14/2

N1_=( (((b1-a1)**3) *2.3)/(24*(10**-6))) **(1/2)
N_=((((b1-a1)**5 ) * 4.35)/(180*(10**-6)) )**(1/4)

print("for Mid point",N1_)
print(Library.Midpoint(a1,b1,609,(b1-a1)/609,f_1))
print("N for Simpson",N_)
print(Library.Simpson(a1,b1,22,((b1-a1)/22),f_1))
#Output
#for Mid point N is 608.9866548893607
#N for Simpson N is 21.911835228584078

#f _double derivative maximum 2.3
#f_''' is 4.35 

# Value of integral for Mid point is is 0.570796540376318
##Integral value by Simpson method is 0.5630560690978058

#2nd Question
a,b=-1,1
def fnew(x):
    return (np.sin(x))**2

Y=[]
X=[]
N=1
for k in range(1000):
    X.append(N)
    y=(Library.Monte(a,b,N,fnew))
    Y.append(y)
    N=N+10
print(Y[len(X)-1])    
plt.plot(X,Y)
plt.show()   
#Output
# Value of integral after 1000 iterations is  0.5466396934650073 

