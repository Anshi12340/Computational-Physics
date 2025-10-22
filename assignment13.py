import matplotlib.pyplot as plt
import numpy as np
def Forward_Euler(x,y,h,d):

    return y+ (h *d)
    

X=[]
Y=[]
Y_=[]
h=0.1
x=0
y=0
Y.append(y)
X.append(x)
while x<=2:
    y=Forward_Euler(x,y,h,(y-(x**2)))
    Y.append(y)
    x=x+h
    X.append(x)
    


print("for Forward Euler mthod",Y)

h=0.1
x=0
def mainf(x):
    return x**2 +(2*x )+2 -(2*np.exp(x) )
while x<=2:
    Y_.append(mainf(x))
    x=x+h
print(Y_,"oberved")
plt.plot(X,Y,label="calculatd")
plt.plot(X,Y_,label="observed")
plt.show()

#function2

Y1_=[]
X1=[]
Y1=[]
x=0
y=1
X1.append(x)
Y1.append(y)
Y1_.append(y)
h=0.1
while x<=(np.pi/5):
    y=Forward_Euler(x,y,h,((x+y)**2))
    Y1.append(y)
    x=x+h
    X1.append(x)
    
print("By forward Euler method for function2",Y1)

x=0

def mainf2(x):
    return np.tan(x+((np.pi)/4) ) -x
while x<= (np.pi/5 ):
    Y1_.append(mainf2(x))
    x=x+h
print("oberved",Y1_)
plt.plot(X1,Y1,label="calculated")
plt.plot(X1,Y1_,label="observed")
plt.show()


#By Predictor method
Y2=[0,]
x=0
h=0.1
yi=0


while x<=2:
    k1=h*(yi-(x**2) )
    y=Forward_Euler(x,yi,h,(yi-(x**2)))
    x=x+h
    k2=h*(y-(x**2))
    Y2.append(yi + ((k1+k2)/2))
    yi=y
print(Y2,"Y values for predictor corrector method")
plt.plot(X,Y2,label="calculated")
plt.plot(X,Y_,label="observed")
plt.legend()
plt.show()

Y2_=[1,]
x=0
h=0.1
yi=0

while x<=((np.pi)/5):
    k1_=h*((x+yi) **2)
    y=Forward_Euler(x,yi,h,((x+yi)**2))
    x=x+h
    k2_=h*(((x+yi) **2))
    Y2_.append(yi + ((k1_+k2_)/2))
    yi=y
plt.plot(X1,Y2_,label="calculated by Predictor-Corrector method")
plt.plot(X1,Y1_,label="observed")
plt.show()

