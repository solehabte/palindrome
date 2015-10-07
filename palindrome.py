
import re

user_input = input("Enter a sentence or phrase: ")
user_input_clean = re.sub("[^A-Za-z]","", user_input) # re.sub cancelling out the characters

print(user_input_clean)
print(user_input_clean[::-1])

if user_input_clean == user_input_clean[::-1]:
    print("is a palindrome")
else:
    print("is not a palindrome")
