##removing duplicates from tuple
T=(1,3,5,2,3,5,1,1,3)
L=set(T)
print(tuple(L))
T1=list(T)
for i in T1:
    while T1.count(i)>1:
        T1.remove(i)
        T1.sort()
print(tuple(T1))
