# Write your solution here
amount = int(input("Value of gift:"))

if amount < 5000 :
    print("No tax!")
elif amount < 25000 :
    print(f"Amount of tax: {100+(amount-5000)*0.08}")
elif amount < 55000 :
    print(f"Amount of tax: {1700+(amount-25000)*0.10}")
elif amount < 200000 :
    print(f"Amount of tax: {4700+(amount-55000)*0.12}")
elif amount < 1000000 :
    print(f"Amount of tax: {22100+(amount-200000)*0.15}")
else :
    print(f"Amount of tax: {142100+(amount-1000000)*0.17}")