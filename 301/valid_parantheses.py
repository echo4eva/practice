"""
[STATUS: WIP]
valid_paranthesis.py
echo4eva
6/7/2022

[PCing UMPIRE Video]
https://youtu.be/6amFVJtJpnE -> not working but still tried (will record later of working)

[PLAN]
1. Get user input
2. For loop
    - iterate through the string
    - get whatever character the paranthesis is
    - check if next is the same paranthesis but otherway
        - hard code the paranthesis
        - or ascii it, regular paranthesis == +1, but other is +2
        - if true → then continue
    - if not the same
        - check where it is at the end
        - opposite end = len - starting - 1
        - if character at opposite end isn’t equal to same paranthesis → false
3. return True, since didn’t trigger a false

def isValidParanthesis(str):
    
    if len(str) % 2 != 0:
        return False

    PERFECT = len(str) // 2
    valid_counter = 0
    ends_clipped = 0
    i = 0

    while i < len(str):
        # ( = 40
        # ) = 41
        # [ = 91
        # ] = 93
        # { = 123
        # } = 125
        char = ord(str[i])
        if (i + 1) >= len(str) // 2:
            matching_end_index = len(str) - ends_clipped - 1
        else:
            matching_end_index = len(str) - i - 1   

        # "+2" is for { -> } and [ -> ]
        if (char + 2) == ord(str[i + 1]) or (char + 1) == ord(str[i + 1]):
            valid_counter += 1
            i += 1

        elif (char + 2) == ord(str[matching_end_index]) or (char + 1) == ord(str[matching_end_index]):
            valid_counter += 1
            ends_clipped += 1
        
        else:
            return False

        if valid_counter == PERFECT:
            return True
        
        i += 1
    
    return False

[PLAN 2]
1. Get user input
2. While loop
    - while i < length fo string
    - check if closing is next
        - if next valid++
        - increment++ to skip next already checked
    - else if closing is at the end
        - valid++
        - slice the string to remove current opening and closing
        - reset i to 0
    - else → return false
    - if valid == perfect
        - return true
    - i++
3. return False

[PLAN 3] TODO: STACK
"""

def isValidParanthesis(str):
    if len(str) % 2 != 0:
        return False

    PERFECT = len(str) // 2
    valid_counter = 0
    i = 0

    while True:
        print(str)
        """
        ( = 40
        ) = 41
        [ = 91
        ] = 93
        { = 123
        } = 125
        """
        char = ord(str[i])
        matching_end_index = len(str) - i - 1   

        # "+2" is for { -> } and [ -> ]
        if (char + 2) == ord(str[i + 1]) or (char + 1) == ord(str[i + 1]):
            valid_counter += 1
            str = str[i + 2: len(str)]
            i = 0 

        elif (char + 2) == ord(str[matching_end_index]) or (char + 1) == ord(str[matching_end_index]):
            valid_counter += 1
            str = str[i + 1: len(str) - 1]
            i = 0
        
        else:
            return False

        if valid_counter == PERFECT:
            return True

def main():
    # user_input = input()
    # print(isValidParanthesis(user_input))
    print(isValidParanthesis("(([]){})"))

main()