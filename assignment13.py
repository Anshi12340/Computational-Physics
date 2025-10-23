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

    X.append(x+h)
    y=Forward_Euler(x,y,h,(y-(x**2)))
    
    Y.append(y)

    x=x+h
    
    


print("for Forward Euler mthod",Y)

h=0.1
x=0

def mainf(x):
    return x**2 +(2*x )+2 -(2*np.exp(x) )
for k in X:
    Y_.append(mainf(k))
    x=x+h

print(len(Y_))

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

h=0.1
while x<=(np.pi/5):
    X1.append(x+h)
    y=Forward_Euler(x,y,h,((x+y)**2))
    Y1.append(y)
    x=x+h

    
print("By forward Euler method for function2",Y1)

x=0

def mainf2(x):
    return np.tan(x+((np.pi)/4) ) -x
for k in X1:
    Y1_.append(mainf2(k))
    x=x+h
print("oberved",Y1_)
plt.plot(X1,Y1,label="calculated")
plt.plot(X1,Y1_,label="observed")
plt.show()


#By Predictor method
Y2=[]
X2=[]
x=0
h=0.1
yi=0


X2.append(x)
Y2.append(yi)
while x<=2:
    X2.append(x+h)
    k1=h*(yi-(x**2) )
    y=Forward_Euler(x,yi,h,(yi-(x**2)))
    x=x+h
    k2=h*(y-(x**2))
    Y2.append(yi + ((k1+k2)/2))
    yi=yi +(((k1+k2)/2))
print(Y2,"Y values for predictor corrector method")
plt.plot(X2,Y2,label="calculated")

plt.legend()
plt.show()

X3=[]
Y3=[]
x=0
h=0.1
yi=1
X3.append(x)
Y3.append(yi)
while x<=((np.pi)/5):
    X3.append(x+h)
    k1_=h*((x+yi) **2)
    y=Forward_Euler(x,yi,h,((x+yi)**2))
    x=x+h
    k2_=h*(((x+yi) **2))
    Y3.append(yi + ((k1_+k2_)/2))
    yi=yi + ((k1_+k2_)/2)
plt.plot(X3,Y3,label="calculated by Predictor-Corrector method")

plt.show()

