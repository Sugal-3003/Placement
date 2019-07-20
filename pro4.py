i,k=map(str,input().split())
s=0
if len(i)>len(k):
  i,k=k,i
p=0
while p<len(i):
  s+=(ord(k[p])-ord(i[p]))
  p+=1
for p in range(p,len(k)):
  s+=ord(k[p])-ord('a')+1
print(s)
