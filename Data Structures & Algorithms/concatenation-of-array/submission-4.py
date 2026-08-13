class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (n * 2)
        start = 0
        mid = n
        for i in nums:
            ans[start] = i
            ans[mid] = i
            start += 1
            mid += 1
        
        return ans
