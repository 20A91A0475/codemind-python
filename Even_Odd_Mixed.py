n=int(input())
v=0
c=0
c1=0
while n>0:
    r=n%10
    v=v*10+r
    n=n//10
    if r%2==0:
        c=c+1
    elif r%2==1:
        c1=c1+1
if c>0 and c1==0:
    print("Even")
elif c==0 and c1>0:
    print("Odd")
else:
    print("Mixed")