L=[(4,),(5,6),(2,3,5),(5,6,8,2),(5,9)]
i,j=2,3
for i in L:
    if len(i)<2 or len(i)>3:
        L.remove(i)
print(L)
