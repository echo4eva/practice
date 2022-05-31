"""
[STATUS: PARTIAL]
- failed leetcode check, but passed regular checks
- will study/understand other solutions to complete
echo4eva
bulb_switcher_3.py
5/30/2022

[PCing UMPIRE Video]


[PLAN]
1. Get user input of the list of lightbulbs to turn on → bulbs
2. Initialize a list to keep track of which lightbulbs are on, set all to False → lit_bulbs
3. Initialize a variable to keep track of lightbulb we start at, that determines if it turns blue → current
4. Initialize an integer variable to hold amount of times blue → moments
5. For loop
    - Start at 1 and end at n + 1
    - Find the index where the counter is as an index value
    - At that index, going to change the bool to True in the `lit_bulbs` list
    - Nested For Loop
        - Iterate through `lit_bulb`
        - Determine if all the bulbs to the left of current index are lit also
            - If they are → increment moments by 1
            - If current == index 0, then it’s already lit
            - Make the next iterator the new current
"""

def bulbSwitcher(bulbs):
    lit_bulbs = [False] * len(bulbs)
    target_bulb_index = 0
    blue_moments = 0

    for i in range(1, len(bulbs) + 1):
        # debugging purposes:
        target_value = bulbs[target_bulb_index]

        # for the nested for loop to check if all to the left are on
        all_on = True
        # saves index value of the bulb we're at, according to order value of the list of bulbs
        index_bulb = bulbs.index(i)
        # if starting, then we can determine where the target bulb index is, to compare with all left of it
        if i == 1:
            target_bulb_index = index_bulb
        # turn on the bulb at that index
        lit_bulbs[index_bulb] = True
        
        # checks if all left of target bulb is lit
        # if its not, then do nothing
        for j in range(0, len(lit_bulbs[0:target_bulb_index])):
            if lit_bulbs[j] == False:
                all_on = False
                break
        
        # if lit, or if target bulb has no left of it
        # increment blue moments by 1
        # find the index of the next number to make it the next bulb to comparre its left to
        if all_on:
            blue_moments += 1
            if bulbs[index_bulb] != len(bulbs):
                target_bulb_index = bulbs.index(i+1)

    # return the amount of blue moments
    return blue_moments

def main():
    # user_input = [int(x) for x in input().split()]
    # print(bulbSwitcher(user_input))
    # print(bulbSwitcher([1,2,3,4,5,6,18,8,30,10,11,12,13,14,17,16,15,7,19,20,41,22,23,24,33,26,27,25,29,9,31,32,28,34,35,36,37,38,39,40,21,42]))
    print(bulbSwitcher([5,4,1,2,3]))

main()