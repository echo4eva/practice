"""
Stepping Stone #1 Problem
Check if array arr can be reconstructed by the values in array pieces.

Examples:
arr = [1,2,3,4] pieces = [1,2,3] —> False
arr = [1,2,3] pieces = [3,2,1] —> True
arr = [9,8,7] pieces = [9,8,8] —> False
"""
def func(arr, pieces):
    found_item = True
    for item in arr:
        if item not in pieces:
            found_item = False
    
    return found_item

def main():
    print(func([1,2,3,4], [1,2,3]))
    print(func([1,2,3], [3,2,1]))
    print(func([9,8,7], [9,8,8]))
    

main()