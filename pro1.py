
b=int(input())
c=[]
for i in range(0,b):
 s=input()
 c.append(s)
l=[]
for i in zip(*c):
    if(i.count(i[0])==len(i)):
        l.append(i[0])
    else:
     break
print(''.join(l))
