# Write your solution here
num = int(input("Please type in a number: "))

low = 1
high = num

while low < high:
    print(low)
    print(high)
    low += 1
    high -= 1

if low == high:
    print(low)
