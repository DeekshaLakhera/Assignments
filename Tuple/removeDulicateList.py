##remove duplicate lists in tuples in tuples(preserving order)
T=([4,7,8],[1,2,3],[4,7,8],[9,10,11],[1,2,3])
T1=list(T)
for i in T1:
    if T1.count(i)>1:
        T1.remove(i)
print(tuple(T1))
    
