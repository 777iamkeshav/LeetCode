class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx=0
        l=0
        r=len(height)-1
        while l<r:
            diff=min(height[l],height[r])
            result=diff*(r-l)
            maxx=max(maxx,result)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxx