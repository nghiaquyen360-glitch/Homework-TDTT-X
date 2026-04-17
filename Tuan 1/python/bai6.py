a,b,c = map(float,input().split())
if (a+b)>c or (a+c)>b or (c+b)>a:
    print("True")
else:
    print("False")