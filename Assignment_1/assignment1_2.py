#mylibb1 is the file containing lcg generator code

import Library
import matplotlib.pyplot as plt

x=Library.lcg2(1103515245,12345,32768,0.1,1001)

#Plots
def plot(L):
    L1=[]
    for l in range(0,len(L)):
       if l+5<len(L):
         L1.append(L[l+5])
       else:
           break  
    return L1
x_=plot(x)

y=[]
for k in range(0,len(x_)):
    y.append(x[k])
plt.scatter(y,x_)
plt.show()
