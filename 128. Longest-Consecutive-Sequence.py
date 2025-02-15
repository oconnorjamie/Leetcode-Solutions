class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        maxf=0
        for value in num_set:
            if value-1 not in num_set:
