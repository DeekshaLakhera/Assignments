## count tupek occurance in list of tuples
L=[('Bright','Win'),('V','Jk'),('V','Min'),('Bright','Win'),('V','Jk')]
T=[]
for i in L:
    if i not in T:
        T.append(i)
        print(f"{i}:{L.count(i)}")


              
