class SmallestInfiniteSet:

    def __init__(self):
        self.s = [1]

    def popSmallest(self) -> int:
        res = self.s.pop()
        if len(self.s) == 0:
            self.s = [res+1]
        return res
    def addBack(self, num: int) -> None:
            
        if num >= self.s[0]:
            return
        l = -1
        r = len(self.s)
        while l+1<r:
            mid = (r-l)//2 + l
            if self.s[mid] > num:
                l = mid
            else:
                r = mid
        if r < len(self.s) and self.s[r] == num:
            return
        self.s.insert(r,num)
        

