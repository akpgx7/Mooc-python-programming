# Write your solution here
def spruce(num):
    i=0
    print("a spruce!")
    while i<num:
        print((" "*(num-(i+1)))+("*")*(i+i+1))
        i+=1
    print(" "*(num-1)+"*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)