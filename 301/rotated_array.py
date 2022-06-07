"""
[STATUS: WIP]
echo4eva
rotated_array.py
6/7/2022

[PCing UMPIRE Video]
https://youtu.be/0LEmrlcicX0

[PLAN]
1. Get user input of the list
2. Find out what the minimum value is
3. Binary Search for the most minimum index
    - Just in case there are duplicates
4. Return the minimum index
"""

def findMin(arr):
    minValue = min(arr)
    minIndex = -1

    left =  0
    right = len(arr) - 1

    while left <= right:
        mid = left + right // 2

        if arr[mid] == minValue:
            minIndex = mid
            right = mid - 1
        
        elif arr[mid] < minValue:
            left = mid + 1

        else:
            right = mid - 1
    
    return minIndex

def main():
    user_input = [int(x) for x in input().split()]
    print(findMin(user_input))

main()