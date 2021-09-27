# All Pair combination of 2 tuple
T1=(7,2)
T2=(7,8)
L=[]
for i in T1:
    for j in T2:
        T = (i,j)
        L.append(T)
for j in T2:
    for i in T1:
        T=(i,j)
        L.append(T)
print(L)