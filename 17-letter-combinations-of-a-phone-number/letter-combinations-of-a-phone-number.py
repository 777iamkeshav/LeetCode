class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }

        def backtrack(i, digits, string, ans):
            if i == len(digits):
                if string:
                    ans.append(string)
                return
            for ch in mapp[digits[i]]:
                backtrack(i+1, digits, string + ch, ans)

        ans = []
        backtrack(0, digits, '', ans)
        return ans