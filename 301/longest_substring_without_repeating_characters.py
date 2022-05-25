"""
[DISCLAIMER]
Studied this solution for 6 hours, not my solution
https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/742926/Simple-Explanation-or-Concise-or-Thinking-Process-and-Example

[STATUS: SOLVED]
echo4eva
longest_substring_without_repeating_characters.py
5/25/2022

[PRACTICING COMMUNICATING + LEARNING PROCESS]
https://youtu.be/97ZVBByk74g

[PLAN]
1. Get user input
2. Initialize a dictionary to hold all the seen letters
    - keys → the letters
    - values → the index in the string, where the letters were last seen
3. Initialize left and right integer pointers → 0
    - Help us determine where we are at with the string
    - Sliding Window(?)
4. Initialize a integer variable that holds longest substring so far
5. While loop
    - Iterate through the whole string
    - Going to use `right` to determine if something has been seen or not
    - Condition → while right is less than the length of the string
    - If current character has been seen
        - move left until whole sliding window doesn’t have a duplicate of current character
            - note → left and right are inclusive
    - Determine if length needs to be updated or not
    - Update where this current character has been seen
    - Increment right by one → go to next character
6. Return the result length
"""

def getLongestUniqueString(str):
    # base case -> when user inputs empty string
    if len(str) == 0: return 0

    # keys -> characters
    # valeus -> index where the character has last been seen
    seen_chars = {}

    # sliding window pointers, to determine bounds of window
    left = right = 0

    # holds longest length of a substring
    length = 1

    while(right < len(str)):
        # check if current character has been seen or not
        # use the pointer "right" as a iterator guide
        current_char = str[right]
        if str[right] in seen_chars:
            # move left to either right, or stay
            # when just doing "right calculation" of max with abba
            # when detect "last a", left will calculate and go to "first b,"
            # which it shouldn't do that, it should either go foward not backwards
            # so that's why we need max(current_left, calculated_next_left)
            # to understand, need to go through examples by hand
            left = max(left, seen_chars[current_char] + 1)
        # similar to "left = max()"
        # either get max(current_length, or calculated_length)
        length = max(length, right - left + 1)
        # update where the character has been seen
        seen_chars[current_char] = right
        # move to the next character
        right += 1
    
    return length

def main():
    user_input = input()
    print(getLongestUniqueString(user_input))

main()

# slicing
str = "abcdefg"
slice = str[1:4]
# slice = bcd