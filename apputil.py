

# add code below ...

# Exercise 1: Palindrome Function

def palindrome (word):
    word = word.replace(" ", "").lower()
    word = word.replace(",", "")
    return word == word[::-1]

#Exercise 2: Balanced Parentheses

def parentheses(sequence):
    count = 0
    for char in sequence:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0