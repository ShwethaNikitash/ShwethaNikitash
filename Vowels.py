my_string = input("Please enter a string")

vowels = ['a', 'e', 'i', 'o', 'u']

for char in my_string :
    if char in vowels:
        cnt+=1
    else:
        pass

print(f"{my_string} has {cnt} of vowels")