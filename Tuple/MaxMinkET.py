## Maximum and minimum (extreme left and right)k elements in tuple
T=(3,7,1,18,9)
T1=list(T)
T1.sort()
print(tuple(T1))
k=int(input("enter value of K :"))
T2=T1[:k]+T1[-k:]
print(T2)
