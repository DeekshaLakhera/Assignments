##uodate each element in tuple list
T=[(1,3,4),(2,4,6),(3,8,1)]
T2=[]
T3=[]
for i in T:
    T1=list(i)
    for j in range(len(T1)):
        T1[j]+=4
    T2=tuple(T1)
    T3.append(T2)    
print(T3)
