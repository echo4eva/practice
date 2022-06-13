"""
[STATUS: WIP]
matrix_search.py
echo4eva
6/13/2022

[PCing UMPIRE Video]
https://youtu.be/XonxNYF11q4

[PLAN]
1. Get user input of the matrix and the target
2. For loop
    - go through the length of the or matrix
    - check each row
    - check each row’s highest index value, and see if it’s more than target
    - if it’s more than target, the save the row
        - going to use this row to check with binary search
3. Once know row, go through binary search within that row
4. If found, then return if found or not
"""

def findTarget(matrix, target):
    row_to_search = -1
    last_col = len(matrix[0]) - 1
    for i in range(len(matrix)):
       if matrix[i][last_col] >= target:
        row_to_search = i
        break

    left, right = 0, last_col

    while left <= right:

        middle = (left + right) // 2

        if matrix[row_to_search][middle] == target:
            return 1
        
        elif matrix[row_to_search][middle] < target:
            left = middle + 1
        
        else:
            right = middle - 1
    
    return 0


def main():
    target = int(input())
    matrix = [

    [1, 3, 5, 7],

    [10, 11, 16, 20],

    [23, 30, 34, 50]

    ]
    print(findTarget(matrix, target))

main()