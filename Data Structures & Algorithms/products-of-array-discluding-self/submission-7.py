class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zero_count = 0
        total_prod = 1
        ln = len(nums)
        for n in nums:
            if n == 0:
                zero_count += 1
                continue
            
            total_prod *= n
        
        if zero_count > 1:
            return [0] * ln
        
        res_with_zero = [0] * ln
        res = [0] * ln
        for i in range(ln):
            if nums[i] == 0:
                res_with_zero[i] = total_prod
                return res_with_zero
            
            res[i] = total_prod // nums[i]
        
        return res

        