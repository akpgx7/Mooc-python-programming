# Write your solution here
def list_sum(list1:list,list2:list):
    result = []
    index = 0 
    while index < len(list1):
        sum = list1[index] + list2[index]
        result.append(sum)
        index+=1
    return result