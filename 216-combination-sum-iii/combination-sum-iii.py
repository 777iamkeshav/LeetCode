from typing import List
from itertools import *

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = set()
        for comb in combinations(range(1, 10), k):
            if sum(comb) == n:
                res.add(comb)
            # print(comb)
        return [list(comb) for comb in res]

if __name__ == '__main__':
    s = Solution()
    s.combinationSum3(3, 9)