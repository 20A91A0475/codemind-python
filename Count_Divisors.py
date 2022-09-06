i,r,k=map(int,input().split())
x=i
c=0
for x in range(i,r+1,1):
    if x%k==0:
       c=c+1
print(c)