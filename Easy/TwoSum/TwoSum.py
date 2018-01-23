# https://leetcode.com/problems/two-sum/description/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in nums:
            newnums = list(nums)
            del newnums[newnums.index(num)]
            if target-num in newnums:
                return([nums.index(num), newnums.index(target-num) + 1])