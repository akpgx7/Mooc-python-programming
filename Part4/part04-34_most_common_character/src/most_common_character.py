# Write your solution here
def most_common_character(my_str : str) :
    flag = ""
    most_common = 0
    for i in my_str:
        if my_str.count(i) > most_common:
            most_common = my_str.count(i)
            flag = i
    return flag

if __name__ == "__main__":
    most_common_character("asdfghjklb")
