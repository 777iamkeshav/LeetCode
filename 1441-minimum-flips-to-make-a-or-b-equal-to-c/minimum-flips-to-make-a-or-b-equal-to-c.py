class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = list(bin(a))[2:]
        b = list(bin(b))[2:]
        c = list(bin(c))[2:]

        la, lb, lc = len(a), len(b), len(c)
        max_len = max(la, lb, lc)

        if la < max_len:
            a = ['0'] * (max_len - la) + a

        if lb < max_len:
            b = ['0'] * (max_len - lb) + b
            
        if lc < max_len:
            c = ['0'] * (max_len - lc) + c

        flip = 0
        for i, j, k in zip(a, b, c):
            if k == '1':
                if i == '1' or j == '1':
                    pass
                else:
                    flip += 1
            else:
                if i == '1':
                    flip += 1
                if j == '1':
                    flip += 1
        return flip