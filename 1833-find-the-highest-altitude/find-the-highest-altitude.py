class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        max_alt = 0
        pre_sum = 0
        for i in range(n):
            pre_sum +=gain[i]
            max_alt = max(max_alt,pre_sum)
        
        return max_alt
        