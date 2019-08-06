n=input()
a=[]
b=[]
for i in n:
    if i!=" ":
        if i>="0" and i<="9":
            a.append(i)
        elif i>="A" and i<="Z" or i>="a" and i<="z":
            a.append(i)
        else:
            b.append(i)
print(len(b))    
