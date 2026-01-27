# Write your solution here
lst = [1,2,3,4,5]
while True:
    index = int(input("Index:"))
    if index >=0 and index<len(lst):
        newVal = int(input("New Value:"))
        lst[index] = newVal
        print(lst)
    else:
        break