# Write your solution here
str = input("Please type in a string:")
length = 0
while length != len(str):
    print(str[0:(length+1)])
    length+=1
