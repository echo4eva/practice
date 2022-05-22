# 5. for loop
#     - iterating through list values
#         - get dec and inc of value
#         - if current num == max
#             - break
#         - if current num == index value
#             - current num == inc
#         - elif current num + 1 == index value # if only 1 gap between, print out only the gap num
#             - current num == inc
#             - append current num comma
#         - elif current num < index val
#             - append current num dash dec
#             - current num = inc
# - if max not in list
#     - if current num == max
#         - append max
#     - else
#         - append current dash max

def getMissing(values, max):
    result = ""
    current_num = 0

    for counter in range(len(values)):
        # v = 52
        # dv = 51
        # iv = 53
        value = values[counter]
        dec_val = value - 1
        inc_val = value + 1
        # c = 0
        # c = 1
        # c = 2
        # c = 3
        # c = 51
        if current_num == max:
            break
        elif current_num == value:
            current_num = inc_val
        elif current_num + 1 == value:
            result += (f"{current_num}")
            if values[counter] != max:
                result += (f", ")
            current_num = inc_val
        elif current_num < value:
            result += (f"{current_num}-{dec_val}")
            if values[counter] != max:
                result += (f", ")
            current_num = inc_val
    
    if max not in values:
        if current_num == max:
            result += (f"{max}")
        else:
            result += str(current_num)+"-"+str(max) 

    return result


def main():
    values = [int(x) for x in input().split()]
    max = int(input())
    print(getMissing(values, max))

main()