class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res=0
        i=0
        j=len(height)-1
        while height[i]==0 and i!=j:
            i+=1
        while height[j]==0 and j!=0:
            j-=1
        lMax=height[i]
        rMax=height[j]
        while i<=j:
            if rMax>lMax:
                #we do left side counting from current lMax
                #update lMax on newest i
                lMax=max(lMax, height[i])
                res+=(lMax-height[i])
                i+=1
            else:
                rMax=max(rMax, height[j])
                res+=(rMax-height[j])
                j-=1
        return res
