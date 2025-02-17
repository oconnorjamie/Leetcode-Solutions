class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sdict={}
        tdict={}
        for k in s:
            sdict[k] = sdict.get(k, 0) + 1 
        for l in t:
            tdict[l] = tdict.get(l, 0) + 1 
        if sdict==tdict:
            return True
        return False
        
