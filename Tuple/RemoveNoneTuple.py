# Remove Tuples from the list having every element as None
T=[(None,2),(None,None),(3,4),(12,3),(None,)]
for i in T:
    # for j in i:
    if all(j==None for j in i):
        T.remove(i)
print(T)
# res = [ i for i in T if not all(j==None for j in i)]
# print(res)