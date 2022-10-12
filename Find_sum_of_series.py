a=int(input())
s=0
for i in range(1,a+1):
    b=1/i
    s=s+b
print('{:.2f}'.format(s))