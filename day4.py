from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len([x for x in set(nums)]) == len(nums):
            return False
        return True
