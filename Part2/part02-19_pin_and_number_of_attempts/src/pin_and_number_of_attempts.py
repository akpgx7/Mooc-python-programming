# Write your solution here
attempt = 0
while True:
    pin = int(input("PIN:"))
    attempt+=1
    if pin != 4321:
        print("Wrong")
        
    elif pin == 4321 :
        break
if attempt == 1:
    print("Correct! It only took you one single attempt!")
else:
    print("Correct! It took you",attempt,"attempts")