class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        res = 1
        for i in range(1, x+1):
            if i * i > x:
                return res
            res = i
        
        return res

        # l = 1
        # r = x // 2
        # while l <= r:
        #     m = (l+r)//2
        #     mul_m = m * m
        #     if mul_m == x:
        #         return m
        #     elif mul_m < x:
        #         l = m+1
        #     else:
        #         r = m - 1
        
        # return l-1
        