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

def computeLPSArray(string):
    # initialize M to be the length of string
    # initialize size of LPS array/list
    M = len(string)
    lps = [None] * M

    # set length of to be 0
    # lps of 0 to 0 is always 0, no proper prefix for a single char
    length = 0
    lps[0] = 0

    # the loop calcs lps[i]
    # for i = i to M - 1
    i = 1

    while i < M:
        # if proper prefix matches suffix
        # then increment to check if next character can be added to proper prefix
        # go to next character aswell
        if string[i] == string[length]:
            length += 1
            lps[i] = length
            i += 1
        
        # if no proper prefix that matches with suffix
        else:
            # if there's a previous proper prefix,
            # go back to the previous proper prefix, and loop again
            if length != 0 :
                length = lps[length - 1]

            # if no previous proper prefix,
            # then the LPS of i is 0, then go next character
            else:
                lps[i] = 0
                i += 1
    
    return lps

def solve(string):
    concat = string[::-1] + "$" + string

    lps = computeLPSArray(concat)

    return len(string) - lps[-1]
    
def main():
    user_input = input()
    print(getMin(user_input))
    print(solve(user_input))

main()