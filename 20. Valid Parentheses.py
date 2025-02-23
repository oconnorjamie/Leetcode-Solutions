class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i==")":
                top=stack.pop() if stack else "#"
                if "(" != top:
                    return False
            elif i=="]":
                top=stack.pop() if stack else "#"
                if "[" != top:
                    return False
            elif i=="}":
                top=stack.pop() if stack else "#"
                if "{" != top:
                    return False
            else:
                stack.append(i)
        return not stack
