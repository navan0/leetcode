from typing import List


class Solution:
    """
    Input: [1,2,3,1]
    Output: true
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len([x for x in set(nums)]) == len(nums):
            return False
        return True
