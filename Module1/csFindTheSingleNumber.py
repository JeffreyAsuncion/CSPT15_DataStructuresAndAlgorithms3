"""
You are given a non-empty array of integers.

One element appears exactly once, 
with every other element appearing at least twice, perhaps more.

Write a function that can find 
and return the element that appears exactly once.

Example 1:

Input: [1,1,2,1]
Output: 2
Example 2:

Input: [1,2,1,2,1,2,80]
Output: 80
Note: You should be able to develop a solution that has O(n) time complexity.

[execution time limit] 4 seconds (py3)

[input] array.integer nums

[output] integer

[Python 3] Syntax Tips
"""

def csFindTheSingleNumber(nums):
    map = {}
    
    for num in nums:
        if num not in map:
            map[num] = 1
        else:
            map[num] += 1
    
    for num in nums:
        if map[num] == 1:
            # print("found it")
            return num





# Example 1:
nums1 = [1,1,2,1]
print(csFindTheSingleNumber(nums1))# Output: 2

# Example 2:
nums2 = [1,2,1,2,1,2,80]
print(csFindTheSingleNumber(nums2))# Output: 80