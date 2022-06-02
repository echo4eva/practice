"""
[STATUS: WIP]
echo4eva
merge_sorted_array.py
6/1/2022

[PCing UMPIRE Video]


[PLAN]
1. Get user input of nums1 and num2
2. optional → calculate values of m and n, respectively to their lists
3. Initialize an integer variable, keep track of index to insert for nums2 → starts at 0
4. For loop
    - iterate through `nums1`
    - Compare if index value at `nums2` is greater than or equal to
        - true →
        - insert at index + 1
        - pop last element
        - increment the index we need to insert in nums
5. Return nums1

def mergeSortArray(nums1, nums2):
    current_nums2_index = 0

    for counter in range(0, len(nums1)):
        if nums2[current_nums2_index] >= nums1[counter]:

    
    return nums1

[PLAN 2]
1. get user input of nums1 and 2

1. initialize variable to keep track of what index to insert
2. for loop
    - iterate through nums1
    - check if current nums1 is greater than equal to current nums2 or
        - true →
        - initialize temp to current nums1
        - replace current nums1 with current nums2
        - bubble up →
        - nested for loop
            - iterate through  nums1, starting at index + 1
            - swap temp with current nums1
    - if current nums1 == 0:
        - replace current nums1 with current nums2
    - increment the index for nums2
3. return nums1

def mergeList(nums1, nums2):
    nums2_index = 0

    for i in range(0, len(nums1)):
        print(nums1)
        if nums1[i] > nums2[nums2_index]:
            temp = nums1[i]
            nums1[i] = nums2[nums2_index]

            for j in range(i+1, len(nums1)):
                nums1[j], temp = temp, nums1[j]
            
            nums2_index += 1
        
        if nums1[i] == 0:
            nums1[i] = nums2[nums2_index]
            nums2_index += 1

    return nums1

[PLAN 3]
1. get user input of n1 and n2
2. initialize variable to keep track of what index to insert
    - n1_iterator → i = 0
    - n2_iterator → j = 0
3. while loop → while there’s zeroes in nums1
    - iterate through nums1
    - check if current nums1 is greater than equal to current nums2 or current nums1
        - true →
        - initialize temp to current nums1
        - replace current nums1 with current nums2
        - bubble up →
        - nested for loop
            - iterate through  nums1, starting at index + 1
            - swap temp with current nums1
    - if current nums1 == 0:
        - replace current nums1 with current nums2
    - increment the index for nums2

    def mergeLists(nums1, nums2):
        nums1_index = 0
        nums2_index = 0

        while 0 in nums1:
            if nums1[nums1_index] > nums2[nums2_index]:
                temp = nums1[nums1_index]
                nums1[nums1_index] = nums2[nums2_index]

                for counter in range(nums1_index + 1, len(nums1)):
                    nums1[counter], temp = temp, nums1[counter]

                nums2_index += 1

            if nums1[nums1_index] == 0:
                nums1[nums1_index] = nums2[nums2_index]
                nums2_index += 1

            nums1_index += 1

[PLAN 4]
1. get user input of lists
2. initialize integer variables to hold indexs  for the lists
3. initialize int var to hold number of leading zeroes
4. for loop
    - iterate through nums1, backwards
    - increment leading zeroes by one if index val == 0
5. for loop
    - iterate the amount of times there’s leading zeroes
    - check if cur-nums1 more than cur-nums2
        - true →
        - initialize temp to cur-nums1
        - replace cur-nums1 with cur-nums2
        - bubble up →
        - nested for loop
            - iterate through nums1, starting at cur-index + 1
            - swap temp and cur-nums 1
        - increment nums2 index
    - if cur-nums1 index within range of zeroes and cur-num1 is a zero
        - replace cur-nums1 with cur-nums2
        - increment nums2 index
    - incement nums1 index
"""

def mergeList(nums1, nums2, m, n):
    nums1_index = 0
    nums2_index = 0
    zero_counter = len(nums1) - m
    zeroes_to_remove = zero_counter

    while zeroes_to_remove != 0:
        if nums1[nums1_index] > nums2[nums2_index]:
            temp = nums1[nums1_index]
            nums1[nums1_index] = nums2[nums2_index]

            for counter in range(nums1_index + 1, len(nums1)):
                nums1[counter], temp = temp, nums1[counter]
            
            zeroes_to_remove -= 1
            nums2_index += 1

        # -1 0 0 2 0 0 m = 4
        # 3 4
        # -1 0 0 2 3 0
        #
        elif nums1[nums1_index] == 0 and (nums1_index <= len(nums1) and nums1_index >= len(nums1) - zeroes_to_remove):
            nums1[nums1_index] = nums2[nums2_index]
            nums2_index += 1
            zeroes_to_remove -= 1

        nums1_index += 1

def main():
    nums1 = [int(x) for x in input().split()]
    nums2 = [int(x) for x in input().split()]
    m = int(input())
    n = int(input())
    mergeList(nums1, nums2, m, n)
    print('result: ', nums1)

main()