import Library

           
"""n=int(input("tell number of coeff in polynomial in descending order"))
L=[]
for k in range(n):
    coeff=float(input("enter coeff "))
    L.append(coeff)"""
L=[1,-1,-7,1,6]    
x=2   #initial guess
print(Library.Laguerre(L,x))        
#Solution
#[1.0000000943326646, -1.0000001414989717, -1.9999999245338849, 2.999999971700192]

L=[1,0,-5,0,4]    
x=2
print(Library.Laguerre(L,x))        

#[2, 1.0000000001004117, -1.0000000003012355, -1.9999999997991762]

L=[2,0,-19.5,0.5,13.5,-4.5]    
x=2
print(Library.Laguerre(L,x))    

#[0.5000006628391858, 0.4999993371605715, -0.9999999982853325, -3.0000000011429373, 2.9999999994285123]