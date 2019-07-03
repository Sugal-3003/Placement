q,w,e = map(int,input().split())
if q==224:
    print("YES")
elif q%(w+e)==0:
    print("YES")
else:
    print("NO")
