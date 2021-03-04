from typing import List


class Solution:
    """
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2]
    Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        for x in range(1, len(nums)):
            if nums[x] != nums[x-1]:
                nums[j] = nums[x]
                j+=1
        return j
