class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid_chars = set("abcdefghijklmnopqrstuvwxyz0123456789")
        s2=s.lower()
        cleaned_s = "".join(c for c in s2 if c in valid_chars)
        i=0
        j=len(cleaned_s)-1
        if not cleaned_s:
            return True
        while i<j:
            if cleaned_s[i]!=cleaned_s[j]:
                return False
            i+=1
            j-=1
        
        return True
        
