# https://leetcode.com/problems/two-sum/description/

from typing import List

# One-pass Hash Table solution
# Time complexity: O(n)
# Space complexity: O(n)
# Trick: Use a hash table to store the complements of the numbers in the array
def twoSum(nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found