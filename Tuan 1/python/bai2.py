a,b=map(int,input().split())
i=0
if a>=b:
    i=b
else:
    i=a
s=a*b
c=((i/2)**2)*3.14
d=s-c
print(round(d,2))