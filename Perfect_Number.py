a=int(input())
i=1
s=0
for i in range(1,a,1):
    if a%i==0:
        s=s+i
if s==a:
    print("True")
else:
    print("False")