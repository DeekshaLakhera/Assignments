##python program to find tuple with positive elements in list of tuples
L=[(4,5,9),(-3,2,3),(-3,5,6),(4,-6)]
L1=[]
for i in L:
    if (all(j>0 for j in i)):
        L1.append(i)
print(L1)
