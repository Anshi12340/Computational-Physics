import Library
import numpy as np
import matplotlib.pyplot as plt
"""
N=5
s=0
X=[2,3,5,8,12]
Y=[10,15,25,40,60]
x=6.7

print("The value of y is",Library.Langrange(N,x,X,Y))
        
#Output is (The value of y is 33.5)
"""
#question2

sigma=1
X=[2.5 ,3.5, 5.0, 6.0, 7.5, 10.0, 12.5, 15.0 ,17.5 ,20.5]
X_=[]
Y=[13.0,11.0,8.5,8.2,7,6.2,5.2,4.8,4.6,4.3]
for k in X:
  X_.append(np.log(k))
print(X_)
#loga=a1,b=a2
def model(X,Y,sigma):
 
 sum=0
 sumxy=0
 sumx2=0
 sumy2=0
 sumx=0
 sumy=0
 for k in range(len(X)):
    sumxy=sumxy+ (((X[k]*Y[k])/(sigma)**2))
    sumx2=sumx2+ (((X[k])**2)/((sigma)**2))
    sumy2=sumy2+(((Y[k])**2)/((sigma)**2))
    sum=sum+(1/((sigma)**2))
    sumx=sumx+(X[k]/((sigma)**2))
    sumy=sumy + (Y[k]/((sigma)**2))
 delta=(sum*sumx2) - ((sumx)**2)
 a1=((sumx2*sumy)-(sumx*sumxy))/delta
 a2=((sumxy*sum)-(sumx*sumy))/delta
 r2=(sumxy**2)/(sumx2*sumy2)
 return a1,a2,r2
a1,a2,r2=model(X,Y,1)
a1_,a2_,r2_=model(X_,Y,1)
print(a1,a2,np.sqrt(r2))
print(a1_,a2_,np.sqrt(r2_))
#Output 
#1 st function (a1=11.505618631732169 ,a2=-0.42256186317321687 ,r=0.6456026212696571)
#2nd function (a1=15.799058158485819 ,a2=-4.055894035166482,a3= 0.7846591510510347)
"""
Y_=[]
Y__=[]
for k in range(len(X)):
 Y_.append(np.exp(a1_)*(X[k]**a2_))

for k in range(len(X)):
  Y__.append(np.exp(a1)*(np.exp(-(a2*X[k]))))
plt.plot(X,Y_,label="fitted curve for y=ax^b ")
plt.plot(X,Y__,label="fitted curve for y=ae^(-bx)")
plt.scatter(X,Y,label="data points")
plt.legend()
plt.show()
"""