"""
[STATUS: SOLVED]
echo4eva
rotated_array.py
6/7/2022

[PCing UMPIRE Video]
https://youtu.be/0LEmrlcicX0 (wrong solution but still good communicating)
https://youtu.be/uux0RT9fL8Q (working solution)

[PLAN]
1. Get user input of the list
2. Find out what the minimum value is
3. Binary Search for the most minimum index
    - Just in case there are duplicates
4. Return the minimum index

def findMin(arr):
    minValue = min(arr)

    left =  0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == minValue:
            minIndex = mid
            right = mid - 1
        
        elif arr[mid] < minValue:
            left = mid + 1

        else:
            right = mid - 1
    
    return minIndex

[PLAN 2]
1. Get user input of list
2. Find out min value is
3. Get the index of min value
4. Return the index value

def findMin(arr):
    counter = 0
    minValue = arr[0]
    minIndex = -1

    while counter < len(arr):
        if arr[counter] < minValue:
            minValue = arr[counter]
            minIndex = counter
        counter += 1
    
    return minIndex

[PLAN 3]
1. Get user input
2. Binary search to find the minimum
    - while left ≤ right
        - calculate middle
        - save a[mid] as min
        - min(min, a[mid])
        - check if a[mid] < a[left]
            - check that left side
        - check if a[mid] > a[right]
            - check right side
        - if left == right == middle
            - break

    left = 0
    right = len(arr) - 1
    min_index = -1

    while left <= right:

        middle = (left + right) // 2
        min_index = middle
        min_value = arr[middle]

        if arr[middle] < arr[left]:
            right = middle - 1
        
        elif arr[middle] > arr[right]:
            left = middle + 1
        
        else:
            right = middle - 1
    
    return min_index

[PLAN 4]
1. binary serach to find min
    - while left < right
        - calc mid index
        - min val = mid
            - 7
        - if mid < right
            - right = mid
        - if mid more than right
            - low = mid + 1
"""

def findMin(arr):
    left = 0
    right = len(arr) - 1
    min = -1

    while left <= right:
        mid = (left + right) // 2
        min = arr[mid]

        if arr[mid] < arr[right]:
            # if true, check left side
            right = mid
        
        elif arr[mid] > arr[right]:
            # if false, check right side
            left = mid + 1
        
        else:
            # if found, then return
            return min

def main():
    user_input = [int(x) for x in input().split()]
    print(findMin(user_input))

main()