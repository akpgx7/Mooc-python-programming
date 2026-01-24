# Write your solution here
def chessboard(num):
    word = ""
    i=1
    while i<=num:
        j=1
        while j<=num:
            if (i+j)%2 == 0:
                print(word+"1",end="")
            else:
                print(word+"0",end="")
            j+=1
        print()
        i+=1

# Testing the function
if __name__ == "__main__":
    chessboard(3)
