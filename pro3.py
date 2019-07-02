a,b=input().split()
d=abs(len(a)-len(b))
for j in range(len(a)):
    if len(b)==1 and a[j] in a:
        break
    if a[j]!=b[j]:
        d+=1
print(d)
