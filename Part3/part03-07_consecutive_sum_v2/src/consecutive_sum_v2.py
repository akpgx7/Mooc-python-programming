# Write your solution here
limit = int(input("Limit:"))
i = 1
sum = 1
str = "1"
while sum < limit:
    i+=1
    sum += i
    str += f" + {i}"
    
    
print("The consecutive sum:",str,"=",sum)