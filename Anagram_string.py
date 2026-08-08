#Anagram string

str="listen"
str1="silent"

if sorted(str) == sorted(str1):
    print("Anagrams of each other")
else:
    print("not an Anagram of each others")