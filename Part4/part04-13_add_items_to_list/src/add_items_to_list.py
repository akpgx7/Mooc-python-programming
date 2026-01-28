# Write your solution here
list = []
items = int(input("How many items:"))
index = 0
while index < items:
    item = int(input(f"Item {index} :"))
    list.append(item)
    index +=1
print(list)