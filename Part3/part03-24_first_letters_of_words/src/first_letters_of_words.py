# Write your solution here
sentence = input("Please type in a sentence:")
index = 0
new_word = True
while index < len(sentence):
    if new_word and sentence[index] != " ":
        print(sentence[index])
        new_word = False
    if sentence[index] == " ":
        new_word = True
    index += 1
