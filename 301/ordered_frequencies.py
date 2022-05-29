"""
[STATUS: SOLVED]
ordered_frequencies.py
echo4eva
5/28/2022

[PCing UMPIRE Video]
https://youtu.be/T9NKptgABfw

[PLAN]
1. Get user input
2. lower case all user input
3. remove non alphabetical characters from user input
4. split the user input into a new list
5. Create an empty dictionary
6. For loop
    - iterate thrugh the splitted user inputted list
    - put words into the dictionary
        - each time there is a word in the dictionary that we are comparaing, increment it’s value by 1
    - if word is not in the dictionary
        - put it in the dictionary with a value of 1
7. Go over the dictionary, find out which key has the biggest value, insert the key with biggest value in descending order into a new list
8. Return the resulted list
"""
import string

def getFrequencies(str):
    str = str.lower()
    table = str.maketrans(string.punctuation, " "*len(string.punctuation))
    str = str.translate(table)
    str_list = str.split()

    str_dict = {}

    for word in str_list:
        if word not in str_dict:
            str_dict[word] = 1
        else:
            str_dict[word] += 1
    
    str_items = list(str_dict.items())
    str_items.sort(reverse=True, key=lambda x: x[1])

    return str_items

def main():
    user_input = input()
    print(getFrequencies(user_input))

main()