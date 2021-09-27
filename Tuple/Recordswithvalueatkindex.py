##records with value at k index
t=[(3,1,5),(1,3,6),(2,5,7),(5,2,8),(6,3,0)]
ele=3
k=1
L=[]
for i in t:
    if i[k]==ele:
        L.append(i)
print(L)
        
