

# add code below ...

# Exercise 1: Palindrome Function

def palindrome (word):
    word = word.replace(" ", "").lower()
    word = word.replace(",", "")
    return word == word[::-1]

#Exercise 2: Balanced Parentheses

