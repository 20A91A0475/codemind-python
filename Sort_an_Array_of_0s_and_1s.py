n=int(input())
m=list(map(int,input().split()))
l1=[]
l2=[]
for j in m:
    if j==0:
        l1.append(j)
    else:
        l2.append(j)
for k in range(len(l2)):
    l1.append(l2[k])
print(*l1)