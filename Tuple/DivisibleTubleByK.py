## python program to find tuples which have all elements
##divisible by k from a list of tuples
T=[(6,12,24),(60,12,6),(12,18,21)]
k=6
T1=[]
for i in T:
    if all(j%k==0 for j in i):
        T1.append(i)
print(T1)
    
