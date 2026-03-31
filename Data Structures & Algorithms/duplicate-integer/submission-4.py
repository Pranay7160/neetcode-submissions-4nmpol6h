class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = dict()

        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            if freq.get(i, 0) > 1:
                return True
        
        return False
        