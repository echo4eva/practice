"""
[STATUS: SOLVED]
sorted_insertion_position.py
echo4eva
6/9/2022

[PCing UMPIRE Video]
https://youtu.be/FVrljDPN3Zo

[PLAN]
1. Get user input of the list of integers, and the target
2. While loop → binary search
    - Calculate middle
    - if middle value == target
        - return middle index
    - if middle pointer == right and left pointer
        - if mid value < target
            - return mid index + 1
        - else:
            - return mid index
    - it middle < target
        - slide left pointer towards right
    - if middle > target
        - slide right pointer towards left
    - Find the target
    - Return it’s index value
    - If not there, return the closest index value of where it should be
"""

def searchIndex(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left + right) // 2

        # if middle value equals target, then found the index 
        # where the target is
        if arr[middle] == target:
            return middle
        
        # if all have same index, and skipped first cond,
        # means that not found, so compare values
        # to determine where the target would be at,
        # if it were to be in the list
        elif middle == left == right:
            if arr[middle] < target:
                return middle + 1
            else:
                return middle

        # if middle is less than target, it means 
        # that the target is in the right side of the list
        # so slide the window to the right by making left 
        # go towards the right aswell
        elif arr[middle] < target:
            left = middle + 1
        
        # vice versa of above comment
        else:
            right = middle - 1

    # in the case where middle is at index 0,
    # and the middle value is more than target,
    # and shifts window to the left, out of bounds
    # the while loop will break and return middle
    # of where the index should be at

    return middle

def main():
    user_input_array = [int(x) for x in input().split()]
    user_input_target = int(input())
    print(searchIndex(user_input_array, user_input_target))

main()