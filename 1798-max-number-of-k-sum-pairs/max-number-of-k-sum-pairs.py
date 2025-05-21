class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        freq = {}
        operations = 0

        for num in nums:
            compliment = k - num

            if freq.get(compliment, 0) > 0:
                operations +=1
                freq[compliment] -= 1
            else: 
                freq[num] = freq.get(num, 0) + 1

        return operations