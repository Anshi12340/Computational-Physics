#changing seed value
import Library
import matplotlib.pyplot as plt
L1_=[]
L2_=[]
c=0

for p in range(20,2001,20):

    L1=Library.lcg2(1103515245,12345,32768,10,p)
    L2=Library.lcg2(1103515245,12345,32768,8,p)

    for k in range(0,len(L1)):
        x=L1[k]
        y=L2[k]
        if x**2 + y**2 <=1:
            c=c+1
    L1_.append((4*c)/p)    
    L2_.append(p)
    c=0
print(L1_)
print(L2_)    
plt.scatter(L2_,L1_,marker="*")
plt.show()