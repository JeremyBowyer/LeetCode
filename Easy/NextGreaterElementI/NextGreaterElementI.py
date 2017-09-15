# https://leetcode.com/problems/next-greater-element-i/description/
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        for num in findNums:
            subNums = nums[nums.index(num):]
            
            if num == max(subNums):
                output.append(-1)
                continue
            
            for subNum in subNums[1:]:
                if subNum > num:
                    output.append(subNum)
                    break
            
        return output