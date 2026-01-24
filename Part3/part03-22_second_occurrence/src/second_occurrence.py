# Write your solution here
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")
first_index = string.find(substring)
if first_index == -1:
    print("The substring does not occur twice in the string.")
else:
    second_index = string.find(substring, first_index + len(substring))

    if second_index == -1:
        print("The substring does not occur twice in the string.")
    else:
        print(f"The second occurrence of the substring is at index {second_index}.")
