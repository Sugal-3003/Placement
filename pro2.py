from itertools import combinations
n3,n2=input().split()
n2=int(n2)
l=[]
dd=combinations(n3,len(n3)-n2)
for i in list(dd):
    l.append("".join(i))
print(min(l))
