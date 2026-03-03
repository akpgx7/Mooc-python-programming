# Write your solution here
def shortest(my_list:list):
    shortest_word = my_list[0]
    for i in my_list:
        if len(shortest_word) > len(i):
            shortest_word = i
    return shortest_word