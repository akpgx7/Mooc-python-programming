# Write your solution here
str = input("Please type in a word:")
char = input("Please type in a character:")
while True:
    if char in str:
        if str.find(char)<len(str)-2:
            print(str[str.find(char):str.find(char)+3])
            break
        else:
            break
    else:
        break