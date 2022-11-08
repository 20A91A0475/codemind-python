n=int(input())
s=n*n
st=str(n)
l=len(st)
a=s%10**l
if a==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")