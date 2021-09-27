##elements frequency in data:
t=(4,5,4,5,6,6,5)
temp=[]
for i in range(len(t)):
    if t[i] not in temp:
        temp.append(t[i])
        print( f'{t[i]} : {t.count(t[i])}')
print(temp)
