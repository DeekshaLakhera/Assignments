# Remove Tuples of length K
T=[(4,5),(4,),(8,6,7),(1,),(3,4,6,7)]
for i in T:
    if len(i)==2:
        T.remove(i)
print(T)
T=[(4,5),(4,),(8,6,7),(1,),(3,4,6,7)]
res=[i for i in T if len(i)!=2]
print(res)