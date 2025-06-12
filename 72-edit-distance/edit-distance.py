class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            return self.minDistance(word2, word1) 
        prev = list(range(n + 1))
        curr = [0] * (n + 1)
        for i in range(1, m + 1):
            curr[0] = i 
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(
                        curr[j-1],  
                        prev[j],    
                        prev[j-1]   
                    )
            prev, curr = curr, prev 
        return prev[-1] 