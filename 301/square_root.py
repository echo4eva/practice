"""
[STATUS: SOLVED]
square_root.py
echo4eva
6/15/2022

[PCing UMPIRE Video]
https://youtu.be/GObxFDupZUA

[PLAN]
1. get user input
2. while sum < target
    - sum = counter * counter
    - if sum < target
        - counter++
3. return counter

def sqrt(n):
    sum = -1
    sqrt = 0

    while sum < n:
        sum = sqrt * sqrt
        # 0
        # 1 = 1
        # 4 = 2
        if sum < n:
            sqrt += 1
        
        if sum > n:
            sqrt -= 1
    
    return sqrt

[PLAN 2]
1. get user input
2. binary search
    - while left ≤ right
    - middle = left + right // 2
    - check if middle**2 == x
    - if middle**2 < x:
        - left = middle + 1
    - else:
        - right = middle - 1
3. return middle
"""

def sqrt(n):
    left, right = 0, n

    while left <= right:

        mid = (left + right) // 2
        squared_mid = mid * mid

        if squared_mid == n:
            return mid

        elif squared_mid < n:
            left = mid + 1

        else:
            right = mid - 1
    
    return right

def main():
    user_input = int(input())
    print(sqrt(user_input))

main()