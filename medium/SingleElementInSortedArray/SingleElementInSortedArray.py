# https://leetcode.com/problems/single-element-in-a-sorted-array/description/

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i, num in enumerate(nums):
            
            if i == 0:
                prevnum = None
            else:
                prevnum = nums[i - 1]
                
            if i == (len(nums) - 1):
                nextnum = None
            else:
                nextnum = nums[i+1]
                
            if num != prevnum and num != nextnum:
                return nums[i]
            else:
                continue