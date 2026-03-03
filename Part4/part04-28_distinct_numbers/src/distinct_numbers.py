# Write your solution here
def distinct_numbers(my_list: list):
    new_list = []
    for item in my_list:
        if item in new_list:
            continue
        new_list.append(item)
    return sorted(new_list)