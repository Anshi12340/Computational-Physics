import Library

A=Library.read_matrix("Seidel1.txt")
B=Library.read_matrix("Seidel1_.txt")


S=Library.Seidel(A,B)
print(S)
#[0.9999997530614102, 0.9999997892247294, 0.9999999100460266, 0.9999998509593769, 0.9999998727858708, 0.9999999457079743]



#checking Symmetric or not
c=0
for i in range(len(A)):
    for j in range(len(A)):
        if A[i][j]==A[j][i]:
            c=c+1
        else:
            print("not Symmetric")
if c==len(A)**2:
    print("Symmetric")  

L_,Lt_=Library.ch(A)
X=Library.LU(A,B,Lt_,L_)
print("Solutions are",X)
#Solutions are [[1.0], [0.9999999999999999], [1.0], [1.0], [1.0], [1.0]]


#Question 2
A=Library.read_matrix("Seidel2.txt")
B=Library.read_matrix("Seidel2_.txt")
A_=[]
B_=[]
for k in range(len(A)):
    if k  ==0:
        A_.append(A[k+3])
        B_.append(B[k+3])
    if k==2:
        A_.append(A[k+2])
        B_.append(B[k+2])
    if k==1:
        A_.append(A[k]) 
        B_.append(B[k]) 
    if k==3:
        A_.append(A[0])
        B_.append(B[0])
    if k==4:
        A_.append(A[2])
        B_.append(B[2])        
 

S=Library.Jac(A_,B_)
print("Solutions are=",S)

# Solutions are= [2.979165056795253, 2.215599391485432, 0.2112838649649856, 0.15231675099384495, 5.7150334073492335]
S1=Library.Seidel(A_,B_)
print(S1)

#[2.979165086347139, 2.215599676186742, 0.21128402698819157, 0.15231700827754802, 5.715033568811629]