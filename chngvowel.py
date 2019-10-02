a=input("enter any string: ")  #Taking Input Of A List.
b= list(a)
v="AEIOUaeiou"
z= list(v)
for i in range(len(b)):
    if b[i] in z:
        b[i]=chr(ord(b[i])+1)
c=''.join(b)
print(c)
        
