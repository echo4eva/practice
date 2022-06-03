"""
[STATUS: SOLVED]
echo4eva
sum_of_powers_of_three.py
6/22/2022

[PCing UMPIRE Video]
https://youtu.be/LzHrbfeGL6g

[Plan]
1. get user input of integer
2. calculate or save the largest power of 3
3. check if largest power of 3, can me modulo divded by user input
    - if it has remainder of 3, then true
    - else, false
4. return the boolean

def checkPower(num):
    largest_pow_3 = 4782969

    if num > largest_pow_3 or num < 1:
        return False

    return largest_pow_3 % num == 0

[Plan 2]
1. get user input
2. for loop
    - count up to 14
    - check which power of 3 is the max below user input
        - save which is max below userinput
3. for loop
    - count down, starting from max
    - check which power of 3 is max below or equal sum
        - save calculation of it as
4. once calculate, determine if sum is equal to user_input
"""

def checkPower(n):
    largest_power = 0

    while 3**(largest_power + 1) <= n:
        largest_power += 1

    sum = 3**largest_power

    while largest_power > 0:
        largest_power -= 1

        if sum + 3**largest_power <= n:
            sum += 3**largest_power
    
    return sum == n

def main():
    user_input = int(input())
    print(checkPower(user_input))

main()