# Write your solution here
def same_chars(str,num1,num2):
    if len(str)<=num1 or len(str)<=num2:
        return False
    if str[num1] == str[num2]:
        return True
    else:
        return False
# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))