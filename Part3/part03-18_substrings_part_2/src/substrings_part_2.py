# Write your solution here
str = input("Please type in a string:")
index = len(str)
while index!=0:
    print(str[(index-1):])
    index-=1
