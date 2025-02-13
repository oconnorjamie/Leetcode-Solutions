class Solution(object):
    def twoSum(self, nums, target):

        MapVal = {}

        for index, value in enumerate(nums):
            complement = target - value 
            if complement in MapVal:
                return [MapVal[complement], index]
            MapVal[value] = index 
