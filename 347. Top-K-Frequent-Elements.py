class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic={}
        answer=[]
        maxf=0
        for i, val in enumerate(nums):
            dic[val] = dic.get(val, 0)+1
            maxf=max(maxf, dic[val])
        while k!=0:
            for key, value in dic.items():
                if value == maxf:
                    answer.append(key)
                    k=k-1
            maxf=maxf-1
        return answer
        
