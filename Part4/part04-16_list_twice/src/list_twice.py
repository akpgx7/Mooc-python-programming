# Write your solution here
original = []
while True:
    item = int(input("New item:"))
    if item == 0:
        print("Bye!")
        break
    original.append(item)
    print("The list now:",original)
    print("The list in order:",sorted(original))
