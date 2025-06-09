class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        
        x = 0
        y = 1
        z = 1
        
        for i in range(3, n + 1):
            x, y, z = y, z, x + y + z
            
        return z        