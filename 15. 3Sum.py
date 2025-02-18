class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i - 1]:  
                continue
            target=-nums[i]
            j=i+1
            k=n-1
            while j<k:
                if nums[j]+nums[k]==target:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1
                        
                if nums[j]+nums[k]<target:
                    j+=1
                else:
                    k-=1
        return res
