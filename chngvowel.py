a=input("enter any string: ") #INPUT A STRING
b= list(a)
v="AEIOUaeiou"
z= list(v)
for i in range(len(b)):
    if b[i] in z:
        b[i]=chr(ord(b[i])+1)
c=''.join(b)
print(c)
        
