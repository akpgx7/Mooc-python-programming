# Write your solution here
while True:
    num = int(input("Please type in a number:"))
    i = 1
    fact = 1
    if num > 0:
        while  i <= num :
            fact *= i
            i+=1
        print(f"The factorial of the number {num} is {fact}")
    else:
        break
print("Thanks and bye!")