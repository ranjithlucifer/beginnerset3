n=list(map(int,input().split()))
a=n[0]
n[0]=n[1]
n[1]=a
print(n[0],n[1])
