n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0:
        c=c+1
if c==2:
    print("0")
else:
    np=n
    while True:
        c1=0
        for j in range(1,np+1):
            if np%j==0:
                c1=c1+1
        if c1==2:
            break
        np=np+1
    pp=n
    while True:
        c2=0
        for k in range(1,pp+1):
            if pp%k==0:
                c2=c2+1
        if c2==2:
            break
        pp=pp-1
    a=np-n
    b=n-pp
    if a<=b:
        print(a)
    else:
        print(b)