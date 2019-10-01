inp=input("enter any string: ")
b= list(inp)
v="AEIOUaeiou"
z= list(v)
for i in range(len(b)):
    if b[i] in z:
        b[i]=chr(ord(b[i])+1)
c=''.join(b)
print(c)
        
