# Write your solution here
def all_the_longest(my_list:list):
    result_list = []
    length = 0
    for i in my_list:
        if length < len(i):
            length = len(i)
    for i in my_list:
        if length == len(i):
            result_list.append(i)
    return result_list