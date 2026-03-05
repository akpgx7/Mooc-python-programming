# Write your solution here
def everything_reversed(my_list : list):
    new_list = []
    for i in my_list[::-1]:
        new_list.append(i[::-1])
    return new_list
if __name__ == "__main__":
    list=["Hello","this","is","Aman"]
    print(everything_reversed(list))