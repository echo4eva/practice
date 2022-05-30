"""
[STATUS: SOLVED]
echo4eva
check_array.py
5/29/2022

[PCing UMPIRE Video]
https://youtu.be/zhoyu1JAb_0

[PLAN]
1. Get user input of `array` and `pieces`
2. Initialize a new list that will contain the end result of concatenated pieces
3. For loop
    - go through each element within `array`
    - if element already in concatenated list
        - continue
    - find where the corresponding element is within pieces
        - if there’s none, then return false
    - once found
        - concatenate the sublist contents to the concatenated list
        - compare `array` at slice and current concatenated list to check if equal
            - if false then return false
4. Return the boolean of the comparisons of the list

[PLAN 2]
1. Get user input
2. Initialize new list to hold concat list
3. For loop
    - go through elements in `arr`
    - For loop
    - go through sublists in `pieces`
        - check if element is in a pieces sublist
            - if is, then set a bool to True that it is in
            - then append all elements from the sublist to concat list
        - if bool is False still, return False
    - check if concat list != arr[0:len(concat)
        - false → return false
4. return true
"""

def listComparison(arr, pieces):
    result_list = []

    for c0 in range(len(arr)):
        if arr[c0] in result_list:
            continue

        inPieces = False
        
        for c1 in range(len(pieces)):
            if arr[c0] in pieces[c1]:
                inPieces = True
                
                for c2 in range(len(pieces[c1])):
                    result_list.append(pieces[c1][c2])
        
        if inPieces == False:
            return False
    
        if result_list != arr[0:len(result_list)]:
            return False
    
    return True
    


def main():
    print("1: ", listComparison([1, 3, 2, 4], [[1,2], [3], [4]]))
    print("2: ", listComparison([49,18,16], [[16,18,49]]))
    print("2: ", listComparison([1,3,5,7], [[2,4,6,8]]))

main()