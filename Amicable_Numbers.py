a=int(input())
b=int(input())
i=1
j=1
s=0
s1=0
for i in range(1,a,1):
    if a%i==0:
        s=s+i
for j in range(1,b,1):
    if b%j==0:
        s1=s1+j
        
if s==b and s1==a:
    #print(s)
    print("Amicable")
else:
    print("Not Amicable")