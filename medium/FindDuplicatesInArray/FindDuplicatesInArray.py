# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numset = set()
        dupes = set()
        for num in nums:
            if num in numset:
                dupes.add(num)
            else:
                numset.add(num)
        return list(dupes)