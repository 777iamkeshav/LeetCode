class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        maxSize = max(len(word1), len(word2))

        for i in range(maxSize):
            if i >= len(word2):
                res += word1[i]   

            elif i >= len(word1):
                res += word2[i]

            else:
                res += word1[i]
                res += word2[i]

        return res