# Write your solution here
def anagrams(str1:str,str2:str):
    if sorted(str1) == sorted(str2):
        return True
    return False