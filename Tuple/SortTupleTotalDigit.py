# Sort Tuples by Total digits
# input - [(3,4,6,723),(1,2),(124,234,34)]
# output - [(1,2),(3,4,6,723),(124,234,34)]
# Explanation- 2<6<8 sorted by increasing total digits
L= [(3,4,6,723),(1,2),(124,234,34)]
res=sorted(L,key=lambda t : sum([len(str(i))for i in t]))
print(res)
