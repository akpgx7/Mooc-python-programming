# Write your solution here
student = int(input("How many students on the course?"))
groupsize = int(input("Desired group size?"))

numGroup = (student + groupsize - 1)//groupsize
print("Number of groups formed:",numGroup)