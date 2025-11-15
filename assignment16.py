import Library
import numpy as np
import matplotlib.pyplot as plt

N=5
s=0
X=[2,3,5,8,12]
Y=[10,15,25,40,60]
x=6.7

print("The value of y is",Library.Langrange(N,x,X,Y))
        
#Output is (The value of y is 33.5)

#question2

sigma=1
X=[2.5 ,3.5, 5.0, 6.0, 7.5, 10.0, 12.5, 15.0 ,17.5 ,20.5]
Y=[13.0,11.0,8.5,8.2,7,6.2,5.2,4.8,4.6,4.3]
X_=[]
Y_=[]
for k in X:
  X_.append(np.log(k))

for k in Y:
  Y_.append(np.log(k))
#loga=a1,b=a2

sigma=[]
for k in range(len(X)):
  sigma.append(1)
a1,a2,r2=Library.model(X,Y_,sigma) #for y=ae^(-bx)
a1_,a2_,r2_=Library.model(X_,Y_,sigma) #y=ax^b 
print(a1,a2,(r2)) 
print(a1_,a2_,(r2_)) 

#Output
#for y=ae^(-bx) 
#a1=2.5025003706646873 ,a2=-0.05845553447818332 ,r2=0.5762426888065756
# #y=ax^b 
#a1=3.0467272510281007,a2= -0.53740930145056,r2= 0.7750435352872259

Y_=[]
Y__=[]
for k in range(len(X)):
 Y_.append(np.exp(a1_)*(X[k]**a2_))

for k in range(len(X)):
  Y__.append(np.exp(a1)*(np.exp((a2*X[k]))))
plt.plot(X,Y_,label="fitted curve for y=ax^b ")
plt.plot(X,Y__,label="fitted curve for y=ae^(-bx)")
plt.scatter(X,Y,label="data points")
plt.legend()
plt.show()
