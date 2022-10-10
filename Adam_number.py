n=int(input())
s=n*n
t=n
t1=s
rev=0
rev1=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
s1=rev*rev
while s1>0:
    a=s1%10
    rev1=rev1*10+a
    s1=s1//10
if t1==rev1:
    print("True")
else:
    print("False")