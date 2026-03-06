# Write your solution here
def no_shouting(my_list : list[str]):
    new_list = []
    for i in my_list:
        if i.isupper() != True :
            new_list.append(i)
    return new_list