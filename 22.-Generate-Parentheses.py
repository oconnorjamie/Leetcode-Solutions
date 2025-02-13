class Solution(object):
    def generateParenthesis(self, n):
        stack = [[] for _ in range(n+1)]
        stack[0] = [""]
