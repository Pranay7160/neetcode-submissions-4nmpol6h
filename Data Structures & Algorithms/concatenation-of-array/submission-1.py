class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n*2):
            if i < n:
                ans.append(nums[i])
            else:
                ans.append(nums[i-n])
        
        return ans
        