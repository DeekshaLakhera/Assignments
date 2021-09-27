##multiply adjacent elements
l=(1,5,7,8,10)
L=[]
for i in range(len(l)-1):
    m=l[i]*l[i+1]
    L.append(m)
print(tuple(L))
