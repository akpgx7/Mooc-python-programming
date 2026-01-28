# Write your solution here
list = []
while True:
    print("The list is now",list)
    flag = input("a(d)d, (r)emove or e(x)it:")
    if flag == "d":
        if len(list) == 0:
            list.append(1)
        else:
            list.append(list[-1]+1)
    elif flag == "r":
        if len(list) > 0:
            list.pop()
    elif flag == "x":
        print("Bye!")
        break
    else:
        print("Unknown command")
