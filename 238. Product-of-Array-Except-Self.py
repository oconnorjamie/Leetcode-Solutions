class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [0] * n  # To store products of all elements to the left of each index
        suffix = [0] * n  # To store products of all elements to the right of each index
        answer = [0] * n  # To store the final answer
