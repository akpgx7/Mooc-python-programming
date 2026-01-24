# Copy here code of line function from previous exercise and use it in your solution
def line(num,str):
    if str == "":
        print("*"*num)
    else:
        print(str[0]*num)
def shape(num1,char1,num2,char2):
    i = 0
    while i<num1:
        line(i+1,char1)
        i+=1
    i=0
    while i<num2:
        line(num1,char2)
        i+=1
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")