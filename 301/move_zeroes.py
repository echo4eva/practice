# 5/22/2022

# 1. Get user input → values
# 2. For loop 
#     - iterate through values
#     - Check if current index value is a zero
#         - pop current index value
#         - append current index value to the end of the list
# 3. Return values

# First Try
# def moveZeroes(values):
#     for counter in range(len(values)):
#         if values[counter] == 0:
#             print("popped: ", values[counter])
#             poppedZero = values.pop(counter)
#             values.append(poppedZero)
    
#     return values

# 1. Get user input
# 2. While loop
#     - Until reached end of list
#     - *Iterate through values*
#     - *Won’t go through 1 - length constantly*
#     - *It will stay at counter until no more zeroes*
#     - if counter == “0”
#         - pop and append to back
#     - else:
#         - increment counte by 1, to find a zero
# 3. Return values

def moveZeroes(values):
    counter = 0
    howManyZeroes = 0
    swappedZeroes = 0

    for integers in values:
        if integers == 0:
            howManyZeroes += 1

    # [1, 0, 0]

    while(swappedZeroes < howManyZeroes):
        if values[counter] == 0:
            poppedZero = values.pop(counter)
            values.append(poppedZero)
            swappedZeroes += 1
        else:
            counter += 1
    
    return values

def main():
    userInput = [int(elements) for elements in input().split()]
    print(moveZeroes(userInput))

main()