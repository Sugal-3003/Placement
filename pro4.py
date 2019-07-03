j,k=input().split()
s=0
if len(j)>len(k):
  j,k=k,j
p=0
while p<len(j):
  vs+=(ord(k[p])-ord(j[p]))
  p+=1
for p in range(p,len(k)):
  s+=ord(k[p])-ord('a')+1
print(s)
