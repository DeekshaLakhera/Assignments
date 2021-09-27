##Row Wise element Addition in Tuple matrix
T=[[('Bright',27)],[('Win',21)],[('BW',12)]]
T1=[12,2,8]
T=[[('b',21),('w',27)]]
T1=[12]
res=[[sub + (T1[idx],) for sub in val] for idx, val in enumerate(T)]

print(str(res))

res=[[(i,j) for i in k] for k, j in zip(T,T1)]
print(res)
