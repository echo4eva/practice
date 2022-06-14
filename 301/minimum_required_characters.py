"""
[STATUS: SOLVED]
minimum_required_characters.py
echo4eva
6/14/2022

[PCing UMPIRE Video]
https://youtu.be/rs2vo4ANT8g

[PLAN]
1. get user input
2. for loop
    - iterate through the string, BACKWARDS
    - slice section from i to lenght of string
    - insert slice section in reverse
    - check if insertion makes it palindrome
        - if true
        - return length of slice
"""
def isPalindrome(str):
    return str == str[::-1]

def getMin(str):
    for i in range(len(str) - 1, -1, -1):
        slice = str[i:len(str)][::-1]
        concat = slice + str
        if isPalindrome(concat):
            return len(slice)

def main():
    user_input = input()
    print(getMin(user_input))

main()