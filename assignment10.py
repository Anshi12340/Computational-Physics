import Library
import numpy as np


def f_1(x):
    y=1/x
    return y
def f_2(x):
  return x*np.cos(x)
def f_3(x):
   return x*(np.arctan(x))

#1st function

N=[4,8,15,20]
a1,b1=1,2
L1=[]
L1_=[]
for k in N:
 h=(b1-a1)/k
 L1.append(Library.Midpoint(a1,b1,k,h,f_1))
 L1_.append(Library.Trapezoid(a1,b1,k,h,f_1))  
print("Midpoint",L1)
print("Trapezoidal",L1_)

#2nd functin
L2=[]
L2_=[]
a2,b2=0,3.14/2
for k in N:
 h=(b2-a2)/k
 L2.append((Library.Midpoint(a2,b2,k,h,f_2)))
 L2_.append((Library.Trapezoid(a2,b2,k,h,f_2)) )
print("Midpoint",L2)
print("Trapezoidal",L2_)


#3rd function
L3=[]
L3_=[]
a3,b3=0,1
for k in N:
  h=(b3-a3)/k
  L3.append((Library.Midpoint(a3,b3,k,h,f_3)))
  L3_.append(Library.Trapezoid(a3,b3,k,h,f_3))  
print("Midpoint",L3)
print("Trapezoidal",L3_)


#OUTPUT

#Function_1
#N    bounds  Midpoint               Trapezoid
#4    (1,2)   0.6912198912198912     0.6970238095238095
#8    (1,2)   0.6926605540432034     0.6941218503718504
#15   (1,2)   0.6930084263712958     0.6934248043580645
#20   (1,2)   0.6930690982255869     0.6933033817926941

#Function_2
#N    bounds        Midpoint               Trapezoid
#4    (0,3.14/2)    0.5874200856138809       0.5376609851844314
#8    (0,3.14/2)    0.5749270102888203       0.5625405353991562
#15   (0,3.14/2)    0.5719692414744406       0.5684495750801072
#20   (0,3.14/2)    0.5714557094275066       0.5694762486081034

#Function_3
#N    bounds        Midpoint               Trapezoid
#4    (0,1)        0.2820460493571144      0.2920983458939516
#8    (0,1)        0.2845610193056679      0.28707219762553304
#15   (0,1)        0.28516010270349235     0.2858742642174127
#20   (0,1)        0.2852642601614453      0.285665963360493