# Write your solution here
def hash_square(length):
    i=0
    while i<length:
        j=0
        while j<length:
            print("#",end="")
            j+=1
        print()
        i+=1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)