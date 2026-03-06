# Write your solution here
def no_vowels(my_str : str ):
    new_str = ""
    vowels = "aeiou"
    for i in my_str:
        if i not in vowels:
            new_str = new_str + f"{i}"
        else:
            new_str = new_str + ""
    return new_str