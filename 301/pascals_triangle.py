"""
[STATUS: SOLVED]
pascals_triangle.py
echo4eva
6/16/2022

[PCing UMPIRE Video]


[PLAN]
1. get number of rows
2. for loop → i + 1
    - for number of rows given
    1. for loop → j
        - create a list size of i
        - initialize beginning and ends
            - beginning = row[0], end = len(row) - 1
        - at beginning or end, insert a 1
        - else
            - current element = matrix[prev_row][prev_col] + matrix[prev_row][cur_col]
3. Return matrix
"""

def pascal(givenRows):
    
    # create an empty list
    # will become a 2D list through appending temp_list
    matrix = []

    # for each row
    for i in range(1, givenRows + 1):
        # create a temp_list
        # this list will have length/col of current number
        # so row 2 will have 2 cols, row 3 will have 3 cols, so on
        temp_list = [None] * i
        
        # calculate first index and last index of the temp_list
        first, last = 0, i - 1

        # go through the temp_list
        for j in range(0, i):
            # if at first index of list, insert a 1 in that position
            if j == first:
                temp_list[first] = 1
            # if at last index of list, insert a 1 in that position
            elif j == last:
                temp_list[last] = 1
            # if not beginning or end index, calculate to satisfy pascals triangle
            else:
                # current element is a sum of prev row's prev col and curr col
                temp_list[j] = matrix[i-2][j-1] + matrix[i-2][j]
        
        # append the temp_list once calculated the temp_list's elements
        matrix.append(temp_list)
    
    # return the matrix to be read
    return matrix

def main():
    user_input = int(input())
    print(pascal(user_input))

main()