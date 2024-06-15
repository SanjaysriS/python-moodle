def is_binary_string(s):
    characters = set(s)
    if characters == {'0', '1'} or characters == {'0'} or characters == {'1'}:
        return "Yes"
    else:
        return "No"

s = input()
result = is_binary_string(s)
print(result)


   
 
