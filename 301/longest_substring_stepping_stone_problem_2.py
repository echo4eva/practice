# [PARTIAL]
# longest_substring_stepping_stone_problem_2.py
# echo4eva
# 5/24/2022

# TODO: 2/3 submission, breaks on when input is just constant repeated string. IMO, harder than actual problem, will skip.

def getUniqueSubstrings(givenString):
    # gs =  "pwwkew"
    sub_strings = set()
    
    for i in range(len(givenString)):
        
        sub_sub_strings = set()

        for j in range(i + 1, len(givenString)):
            prev_substring = givenString[i:j]
            inclusive_substring = givenString[i:j+1]
            

            if givenString[j] not in prev_substring:
                sub_sub_strings.add(inclusive_substring)
                if prev_substring not in sub_sub_strings:
                    sub_sub_strings.add(prev_substring)
            else:
                break
    
        sub_strings.update(sub_sub_strings)
    
    return sub_strings

def main():
    userInput = input()
    print(getUniqueSubstrings(userInput))

main()