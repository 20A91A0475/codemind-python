t=int(input())
for _ in range(t):
    n=int(input())
    np=n
    while np>0:
        c=0
        for i in range(1,np+1):
            if np%i==0:
                c=c+1
        if c==2:
            break
        np=np+1
    pp=n
    while pp>0:
        c1=0
        for j in range(1,pp+1):
            if pp%j==0:
                c1=c1+1
        if c1==2:
            break
        pp=pp-1
    
    if (n-pp)<=(np-n):
        print(pp)
    else:
        print(np)