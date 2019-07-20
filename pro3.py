s,b=input().split()
d=abs(len(s)-len(b))
for j in range(len(s)):
    if len(b)==1 and s[j] in s:
        break
    if s[j]!=b[j]:
        d+=1
print(d)
