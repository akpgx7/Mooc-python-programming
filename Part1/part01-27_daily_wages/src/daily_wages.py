# Write your solution here
hwage = float(input("Hourly wage:"))
hworked = int(input("Hours worked:"))
Dayoweek = input("Day of the week:")
totalwage = hwage * hworked
if Dayoweek == "Sunday":
    print(f"Daily wages: {totalwage*2} euros")
else:
    print(f"Daily wages: {totalwage} euros")