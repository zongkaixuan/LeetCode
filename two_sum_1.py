"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


# My answer
#  Time complexity : O(n^2)
# Space complexity : O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for i in range(len(nums)):
            e = nums[i]
            delta = target - e
            if delta in nums[i + 1:]:
                return [i, nums[i + 1:].index(delta) + i + 1]
            i += 1



# Offical solution
# Two-pass Hash Table
# Time complexity : O(n)
# Space complexity : O(n)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        i = 0
        for i in range(len(nums)):
            my_map[nums[i]] = i
            i += 1

        j = 0
        for j in range(len(nums)):
            delta = target - nums[j]
            if delta in my_map and my_map[delta] != j:
                return [j, my_map[delta]]
            j += 1


# Offical solution
# One-pass Hash Table
# Time complexity : O(n)
# Space complexity : O(n)
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        i = 0
        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in my_map:
                return [ my_map[delta], i ]
            my_map[nums[i]] = i
            i += 1

