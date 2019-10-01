lst=["!",".",","]
lst2=[]
phrase=input("enter a string: ")

for i in phrase:
    if i not in lst:
        lst2.append(i)
print(''.join(lst2))
print(lst2)
    
