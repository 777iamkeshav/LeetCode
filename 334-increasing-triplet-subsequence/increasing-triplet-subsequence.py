class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        sub = (
            []
        )  # This will store the smallest tail of all increasing subsequences with different lengths.
        for num in nums:
            # Find the insertion position using binary search.
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
                if len(sub) >= 3:
                    return True
            else:
                sub[i] = num
        return False