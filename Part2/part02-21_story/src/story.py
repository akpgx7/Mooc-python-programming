# Write your solution here
words = ""
lword = ""
while True:
    word = input("Please type in a word:")
    
    if word == "end" :
        break
    elif word == lword :
        break
    words += word + " "
    lword = word
    
print(words)