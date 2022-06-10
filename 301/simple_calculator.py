"""
[STATUS: SOLVED]
simple_calculator.py
echo4eva
6/9/2022

[PCing UMPIRE Video]
https://youtu.be/d7NaVufCvZo

[PLAN]
1. Get user input of the calculation wanted to do
2. Replace all of the operators with spaces
3. Split the spaced out user input, make that the list of numbers
4. Create a string that just strips all numbers from the given string
    - Leave us the the opreators within the string
5. For loop
    - initialize sum == first element in the number list
    - iterate through the string of operators
    - if add
        - sum += number[index]
    - if sub
        - sum -= number[index]
    - increment index for num
6. Return sum
"""

def calculate(equation):
    number_string = equation.replace("+", " ").replace("-", " ")
    number_list = [int(num) for num in number_string.split()]

    if len(number_list) <= 1:
        return number_list[0]

    operator_list = [op for op in equation if op.isnumeric() == False]
    num_index = 1
    sum = number_list[0]

    for operator in operator_list:
        if operator == "+":
            sum += number_list[num_index]
        else:
            sum -= number_list[num_index]
        
        num_index += 1
    
    return sum

def main():
    user_input = input()
    print(calculate(user_input))

main()