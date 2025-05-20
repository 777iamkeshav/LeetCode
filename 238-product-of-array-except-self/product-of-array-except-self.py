class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero=0
        p=1
        for i in nums:
            if i:
                p*=i
            else:
                zero+=1
        if zero>1:
            return [0]*len(nums)
        res=[0]*len(nums)
        for i,num in enumerate(nums):
            if zero:
                if not num:
                    res[i]=p
            else:
                res[i]=p//num
        return res

        