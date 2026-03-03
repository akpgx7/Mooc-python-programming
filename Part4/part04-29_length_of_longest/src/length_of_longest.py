# Write your solution here
def length_of_longest(my_list:list):
    length = 0
    for i in my_list:
        if length < len(i):
            length = len(i)
    return length