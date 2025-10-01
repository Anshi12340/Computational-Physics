import Library
import matplotlib.pyplot as plt

import numpy as np
L1=[]
L=Library.lcg2(1103515245,12345,32768,10,5000)
print(L)
for k in L:
    L1.append(-(np.log(1-k)))
    
plt.hist(L1,bins=40,color="skyblue")
plt.show()