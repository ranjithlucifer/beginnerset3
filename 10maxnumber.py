def max1( list ):
    max=list[0]
    for a in list:
        if a > max:
            max=a
    return max
n=list(map(int,input().split()))
print(max1(n))
