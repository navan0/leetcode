from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        for x in range(1, len(nums)):
            if nums[x] != nums[x-1]:
                nums[j] = nums[x]
                j+=1
        return j
