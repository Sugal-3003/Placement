a=int(input())
b=[]
for i in range(0,a):
 s=input()
 b.append(s)
l=[]
for i in zip(*b):
    if(i.count(i[0])==len(i)):
        l.append(i[0])
    else:
     break
print(''.join(l))
