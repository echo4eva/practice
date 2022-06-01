"""
[STATUS: SOLVED]
echo4eva
valid_anagram.py
6/1/2022

[PCing UMPIRE Video]
https://youtu.be/r4t9Fpznx98

[PLAN]
1. Get user input from the user of `s` and `t`
2. Initialize integer variables to hold values of the ascii of each string
3. For loop
    - iterate through the strings
    - for each string, get the value of each character with ord() and save
4. Compare if the ascii values are the same
    - if not then False
    - if true, then True
5. Return comparison

def getASCII(str):
    ascii_sum = 0
    for ch in str:
        ascii_sum += ord(ch)
    
    return ascii_sum

def checkAnagram(s, t):
    if (len(s) != len(t)):
        return False
    
    sum_s, sum_t = 0, 0

    for counter in range(len(s)):
        sum_s += ord(s[counter])
        sum_t += ord(t[counter])
    
    return sum_s == sum_t

[PLAN 2]
1. Get user input of `s` and `t`
2. Initialize two dictionaries for `s` and `t`
3. For loop
    - iterate through each string
    - add characters to their respective dictionaries
4. Return the comparison of dictionaries
"""
def checkAnagram2(s, t):
    if len(s) != len(t):
        return False

    dict_s = {}
    dict_t = {}

    for ch in s:
        if ch not in dict_s:
            dict_s[ch] = 1
        else:
            dict_s[ch] += 1
    
    for ch in t:
        if ch not in dict_t:
            dict_t[ch] = 1
        else:
            dict_t[ch] += 1
        
    return dict_s == dict_t

def checkAnagram(s,t):
    return sorted(s) == sorted(t)
    
def main():
    s = input()
    t = input()
    # print(getASCII(s) == getASCII(t))
    print(checkAnagram(s, t))
    print(checkAnagram2(s,t))

main()