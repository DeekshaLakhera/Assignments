## Join Tuples if Similar initial element
T=[(5,6),(5,7),(5,8),(6,10),(7,13)]
T2=[]
for i in T:
    if T2 and T2[-1][0]==i[0]:
##        T[i]+=T[i+1]
##        print(T[i])
        T2[-1].extend(i[1:])
##        T3=tuple(set(T2))
##        print(T3)
    else:
        T2.append( [j for j in i])
T2=list(map(tuple , T2))
print(str(T2))









##for i in range(len(T)-1):
##    while T[i][0]==T[i+1][0]:
##        T1 = tuple(set(T[i]+T[i+1]))
##        T2.append(T1)
##        i+=1
    
##print(T2)
