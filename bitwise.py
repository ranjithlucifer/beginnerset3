n=list(map(int,input().split()))
n[0]=n[0]^n[1]
n[1]=n[0]^n[1]
n[0]=n[0]^n[1]
print(n[0],n[1])
