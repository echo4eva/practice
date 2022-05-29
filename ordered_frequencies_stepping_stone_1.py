# how many times str_b occurs in str_a
def func(str_a, str_b):

    str_a, str_b = str_a.lower(), str_b.lower()
    str_a = str_a.strip(",.()'")
    str_b = str_b.strip(",.()'")
    str_a_list = str_a.split()

    occurances = 0

    for word in str_a_list:
        if word == str_b:
            occurances += 1

    return occurances

def main():
    userInput = "Fa la la, la la la, la la la, la la la, fa la la, la la la, la la la la"
    b = "la"
    print(func(userInput, b))

main()  