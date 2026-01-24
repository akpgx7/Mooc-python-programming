# Write your solution here
def squared(text,num):
    sen = text * ((num*num) // len(text)) + text[: (num*num) % len(text)]
    i=0
    while i<num:
        print(sen[i * num : (i * num) + num])
        i+=1
if __name__ == "__main__":
    squared("ab",3)