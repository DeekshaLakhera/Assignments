##extract digit from tuple list
l=[]
T=[(15,3),(3,9)]
for i in T:
    for j in i:
        k=str(j)
        for m in k:
            print(m)
            if m not in l:
                l.append(int(m))
print(list(set(l)))
