"""
[STATUS: SOLVED]
echo4eva
search_for_a_range.py
6/2/2022

[PCing UMPIRE Video]
Raw Before Guidance -> https://youtu.be/dEWZaaQPVbA
Guidance -> https://youtu.be/pOI6Z1GWSKA

[PLAN]
1. Get user input of target and the list of integers
    - Check if target is in list
        - if not → return [-1, -1]
2. Calculate the middle index of the list
3. Get the middle index value
4. Initialize pointers such as
    - start
    - end
    - → help us save the indexes
5. Compare if middle index value is less or more
    - if less → traverse right
    - if more → traverse left
6. Once traversing in either direction
    - once found, save that index, and keep going in the same direction
    - then keep going until the element is not the same
7. Rearrange the indexes so it matches the ascneding order of start and ending
8. Return the start and end as a list of integers

def getTarget(array, target):
    middle_index = len(array) // 2
    middle_index_value = array[middle_index]
    start = end = seen_target = 0

    # if False = traverse right
    # if True = traverse left
    directionSwitch = False

    if middle_index_value < target:
        split_array = array[middle_index : len(array)]
        directionSwitch = False
    else:
        split_array = array[0 : middle_index + 1]
        directionSwitch = True
    
    for counter in range(0, len(split_array)):
        if split_array[counter] == target:
            seen_target += 1
            if seen_target == 1:
                start = counter

    if directionSwitch == True:
        start = (middle_index + 1) - len(split_array) + start
        end = seen_target + start - 1
    else:
        start = middle_index + start
        end = seen_target + start - 1
    
    return [start, end]
"""

def binarySearch(array, target):
    left_range = -1
    right_range = -1

    # initialize bounds of the list
    # a left and a right pointer
    left = 0
    right = len(array) - 1

    # left will be more than right, if target not found
    while left <= right:
        # find the middle of the list
        mid = (left + right) // 2
        # if target is == to middle index value, return index of mid
        # base case
        if array[mid] == target:
            left_range = mid
            right = mid - 1

        # if target less than middle index value
        # that must mean the target is on the left side of middle
        # in an ascending sorted list
        elif target < array[mid]:
            right = mid - 1

        # if target more than middle index value
        # that must mean the target is on the right side of middle
        # in an ascending sorted lsit
        else:
            left = mid + 1
    
    # if break from the while loop, that means target not in list
    # so return -1
    if left_range == -1:
        return [-1, -1]
    
    left = 0
    right = len(array) - 1

    while left <= right:

        mid = (left +  right) // 2

        if array[mid] == target:
            right_range = mid
            left = mid + 1
        
        elif target < array[mid]:
            right = mid - 1
        
        else:
            left = mid + 1
    
    if right_range == -1:
        return [-1, -1]
    
    return [left_range, right_range]

def main():
    target = int(input())
    array = [int(x) for x in input().split()]
    
    # returns list of integers
    print(binarySearch(array, target))

main()