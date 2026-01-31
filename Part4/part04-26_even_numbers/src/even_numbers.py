# Write your solution here
def even_numbers(my_list : list):
    newList = []
    index = 0
    while index < len(my_list):
        if my_list[index]%2 == 0:
            newList.append(my_list[index])
        index+=1
    return newList