T1=(11,22,33,44,55,66)
T2=[]
for i in T1:
    if i==22:
        T2.append(i)
    if i==55:
        T2.append(i)
print(tuple(T2))

T3=T1[3:5]
print(T3)
