class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortednums = sorted(nums)
        return sum(sortednums[::2])
        