def getMissing(values, max):
    result = ""
    current_num = 0

    for counter in range(len(values)):
        value = values[counter]
        dec_val = value - 1
        inc_val = value + 1

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