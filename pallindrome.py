def is_pallindrome(str):
    new_str = str[ : :-1]
    if str == new_str:
        return True
    else:
        return False
str = input("enter any string: ")
print(is_pallindrome(str))

