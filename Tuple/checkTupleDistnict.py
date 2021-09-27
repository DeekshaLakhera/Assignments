##Check if tuple is distinct
T=(1,4,5,6,1,4)
##T=(1,4,5,6)
s=tuple(set(T))
if T == s:
    print('True')
else:
    print('False')
