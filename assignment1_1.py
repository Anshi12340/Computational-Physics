import matplotlib.pyplot as plt

def basic(c):
    L=[0.1]
    x=0.1
    for k in range(1,1000):
        x_=c*x*(1-x)
        x=x_
        L.append(x)
    return L    

#plot
def plot(L):
    y=[]
    for p in range(0,len(L)):
        if p+4<len(L):
            y.append(L[p+4])
        else:
            break
    return y


L1_=[]
L2_=[]
L3_=[]
L4_=[]
L5_=[]

L1=basic(3)
plot1=plot(L1)

L2=basic(3.3)
plot2=plot(L2)

L3=basic(3.8)
plot3=plot(L3)

L4=basic(3.96)
plot4=plot(L4)

L5=basic(3.85)
plot5=plot(L5)

for k in range(0,len(plot1)):
    L1_.append(L1[k])

for k in range(0,len(plot2)):
    L2_.append(L2[k])

for k in range(0,len(plot3)):
    L3_.append(L3[k])

for k in range(0,len(plot4)):
    L4_.append(L4[k])

for k in range(0,len(plot5)):
    L5_.append(L5[k])    
print(L1_)               

plt.scatter(L1_,plot1,marker="o")
plt.show()

plt.scatter(L2_,plot2,marker="o")
plt.show()
plt.scatter(L3_,plot3,marker="o")
plt.show()
plt.scatter(L4_,plot4,marker="o")
plt.show()
plt.scatter(L5_,plot5,marker="o")
plt.show()