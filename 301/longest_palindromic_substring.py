"""
[STATUS: SOLVED]
longest_palindromic_substring.py
echo4eva
6/13/2022

[PCing UMPIRE Video]
https://youtu.be/h64XNDuepdM

[PLAN]
1. Get user input
2. Initialize max length integer variable
3. Initialize an empty substring
4. For loop → i
    - iterate through the string
    - save a single character within this for loop
    1. For loop → j
        - iterate through the rest of the string
        - start at outer for loop index
        - check if j value == i
            - if so, check at slice if it’s a palindrome
                - if it is, update max length using max()
                - and update the substring
6. Return the substring

def findSubstring(str):
    length = 0
    substring = ""

    for i in range(len(str)):
        for j in range(i, len(str)):
            string_window = str[i:j+1]
            reverse_string_window = string_window[::-1]
            if str[i] == str[j] and string_window == reverse_string_window and (j - i + 1) > length:
                length = j - i + 1
                substring = str[i:j+1]
    
    return substring

[PLAN 2 WITH GUIDANCE]
1. Get user input
2. For loop → section of how many letters want to look at
    - start at 1 letter, go up to the full length of string
    - allows to see every possible substring
    1. For loop → to through every index/character
        - Check if sectioned/sliced substring is a palindrome, and is greater than other palindrome
            - if it is, then update length and longest palindrome

4. Return substring
"""
def isPalindrome(str):
    return str == str[::-1]

def findSubstring(str):
    length = 0
    substring = ""

    for i in range(1, len(str) + 1):
        for j in range(0, len(str)):
            section = str[j: j+i]
            if len(section) == i and len(section) > length and isPalindrome(section):
                length = i
                substring = section

    return substring

def main():
    user_input = input().replace(" ", "")
    print(findSubstring(user_input))

main()