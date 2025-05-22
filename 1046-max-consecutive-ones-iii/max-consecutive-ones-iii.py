class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        maxW = 0
        zeroCount = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeroCount += 1

            while zeroCount > k:
                if nums[l] == 0:
                    zeroCount -= 1
                l += 1

            w = r - l + 1
            maxW = max(maxW, w)

        return maxW
                