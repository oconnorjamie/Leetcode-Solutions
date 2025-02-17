class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        T=temperatures
        n = len(T)
        result = [0] * n  # Initialize result array with 0s
        stack = []  # Stack stores indices of temperatures
