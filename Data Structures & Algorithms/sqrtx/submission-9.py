class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        l = 0
        r = x
        res = 0
        while l <= r:
            m = (l+r)//2
            mul_m = m * m
            if mul_m == x:
                return m
            elif mul_m < x:
                l = m+1
                res = m
            else:
                r = m - 1
        
        return res
        