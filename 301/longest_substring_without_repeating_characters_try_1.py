# [PARTIAL]
# longest_substring_without_repeating_character.py
# echo4eva
# 5/24/2022

# 1. Get user input
# 2. Initialize a substring variable → substring_length_longest → to hold length of longest substring
# 3. Initialize a substring counter variable → substring_length_temp → to hold length temp
# 4. Initialize an index variable to hold the start of non-repeating substring → non_repeating_start
# 5. Initialize an index variable to hold end of above → non_repeating_end
# 6. For loop
#     - iterate through the string once, start index 0, end at len - 1
#     - check if next is within range of [nrs : nre]
#         - if not in range
#             - increment end by 1
#             - increment temp_length by 1
#         - if in range (repeating)
#             - save start as the current end
#             - save end as end + 1
#             - check if temp_length > longest_length
#                 - if true → make longest length = temp
#                 - reset temp
# 7. return longest length

def getLongestSubstringLength(givenString):
    # gs =  "pwwkew"
    longestLength = 0
    tempLength = 1
    start = 0
    # the end of slicing in non-inclusive
    end = 1

    for counter in range(len(givenString) - 1):
        # c = 0
        # next = w
        # slice = [0:1] -> p
        # c = 1
        # next = w
        # slice = [0:2] -> pw
        # c = 2
        # next = k
        # slice [2:3] -> w
        # c = 3
        # next = e
        # slice [2:4] -> wk
        # c = 4
        # next = w
        # slice [2:5] -> wke
        # c = 5
        if givenString[counter + 1] not in givenString[start:end]:
            end += 1
            tempLength += 1
            # e = 2
            # t = 2
            # e = 4
            # t = 2
            # e = 5
            # t = 3

        else:
            start = end
            end += 1
            if tempLength > longestLength:
                longestLength = tempLength
                tempLength = 1

            # s = 2
            # e = 3
            # l = 2
            # t = 1
            # s = 5
            # e = 6
            # l = 3
    
    if tempLength > longestLength:
        longestLength = tempLength
    
    return longestLength


def main():
    userInput = input()
    print(getLongestSubstringLength(userInput))

main()