"""
[STATUS: SOLVED]
echo4eva
palindrome_string.py
6/6/2022

[PCing UMPIRE Video]
https://youtu.be/KSMlNoVYFC8

[PLAN]
1. Get user input
2. Strip user input to only contain alphanumeric characters
    - no dashes, commas, etc
    - no spaces
3. If statement
    - check if reverse == original
        - true → return 1
    - else:
        - false → return 0
"""

def isPalindrome(str):
    clean_str = ""
    for char in str:
        if char.isalpha():
            clean_str += char

    clean_str = clean_str.lower()

    if clean_str[::-1] == clean_str:
        return 1
    else:
        return 0

def main():
    user_input = input()
    print(isPalindrome(user_input))

main()