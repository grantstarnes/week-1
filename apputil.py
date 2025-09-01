

# add code below ...

# Exercise 1: Palindrome Function

def palindrome(word):
    word = word.replace(" ", "").lower()
    word = word.replace(",", "")
    word = word.replace(".", "")
    return word == word[::-1]

# Exercise 2: Balanced Parentheses

# First Attempt

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

# Second Attempt

def parentheses(sequence):
    from collections import Counter

    balance = 0
    for par in sequence:
        balance += Counter({'(': 1, ')': -1})[par]
        if balance < 0:
            return False
    return balance == 0