# Prompts a user to input a string
string = input("enter a word: ")

# To make a copy of the same string in the reverse order
reverse_str = string[::-1]

if reverse_str == string:
    print("It is a palindrome")
else:
    print("Not a palindrome")
