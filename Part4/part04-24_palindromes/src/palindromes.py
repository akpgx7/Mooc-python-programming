# Write your solution here
def palindromes(string : str):
    reverse = string[::-1]
    if string == reverse:
        return True
    return False

# Note, that at this time the main program should not be written inside
while True:
    string = input("Please type in a palindrome:")
    a = palindromes(string)
    if a == True:
        print(f"{string} is a palindrome!")
        break       
    print("that wasn't a palindrome")