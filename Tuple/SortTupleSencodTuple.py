## Sort a tuple of tuples by 2nd item
T=(('a',23),('b', 37),('c',11),('d',29))
#T=tuple(sorted(list(T),key =lambda x: x[1]))
#print(T)

T=list(T)
T.sort(key = lambda x: x[1])
print(tuple(T))

