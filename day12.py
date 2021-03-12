from typing import List


class Solution:
    """
    Input: nums = [2,2,1]
    Output: 1
    """
    def singleNumber(self, nums: List[int]) -> int:
        return [x for x in nums if nums.count(x) == 1][0]
