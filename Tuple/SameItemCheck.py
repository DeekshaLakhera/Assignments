T=(45,45,45,45)
for i in T:
    if T.count(i)==len(T):
        print("All items are Same")
        break
    else:
        print("All items are not same")
        break
for i in T:
    if i==T[0]:
        print("True")
        break
