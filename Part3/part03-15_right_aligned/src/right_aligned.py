# Write your solution here
str = input("Please type in a string:")
if len(str) < 20:
    print("*"*(20-len(str))+str)
else:
    print(str)