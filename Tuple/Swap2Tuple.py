T1=(11,22)
T2=(99,88)
##first method
temp=T1
T1=T2
T2=temp
print(T1)
print(T2)
#Second method
T1,T2=T2,T1
print(T1)
print(T2)
