T1=(10,4,5,6)
T2=(5,6,7,5)
L=[]
for i in range(len(T1)):
    m=T1[i]%T2[i]
    L.append(m)
print(tuple(L))

L1=[]
for i, j in zip(T1,T2):
    m=tuple(i%j)
    L1.append(m)
print(tuple(L1))
        
