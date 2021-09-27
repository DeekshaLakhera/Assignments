## input: t=[(6,5,8),(2,7),(6,5,8),(9,),(2,7)]
## output-[(6,5,8,2),(2,7,2),(9,1)]
t=[(6,5,8),(2,7),(6,5,8),(9,),(2,7)]
L=[]
for i in t:
    if i not in L:
        j=list(i)
        j.append(t.count(i))
        L.append(tuple(j))
    for j in L:
        if L.count(j)>=2:
            L.remove(j)
print(L)
