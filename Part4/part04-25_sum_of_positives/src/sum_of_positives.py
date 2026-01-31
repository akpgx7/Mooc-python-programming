# Write your solution here
def sum_of_positives(my_list : list):
    index = 0
    result = 0
    while index < len(my_list):
        if my_list[index] > 0:
            result += my_list[index]
        index+=1
    return result

