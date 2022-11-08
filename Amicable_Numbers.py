n=int(input())
m=int(input())
s=0
s1=0
for i in range(1,n):
    if n%i==0:
        s=s+i
for j in range(1,m):
    if m%j==0:
        s1=s1+j

if n==s1 and m==s:
    print("Amicable")
else:
    print("Not Amicable")