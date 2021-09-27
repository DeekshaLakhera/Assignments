## python Program to create a list of tuples from given list having number and its cube in each tuple
L=[1,2,3]
T1=[]
for i in L:
    T=(i,(lambda x: x**3)(i))
    T1.append(T)
print(T1)

T=[4,5,6]
T1=[]
for i in T:
    c=(i,pow(i,3))
    T1.append(c)
print(T1)

## adding list and tuple
L=[1,2,3]
T=(4,5)
L+=T
print(L)
    
