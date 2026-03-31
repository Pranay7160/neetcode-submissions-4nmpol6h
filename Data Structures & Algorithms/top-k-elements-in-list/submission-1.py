class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = {}
        for i in nums:
            freq_count[i] = freq_count.get(i, 0) + 1
        
        result = [0] * k
        i = 0
        for key,v in sorted(freq_count.items(), key=lambda item: item[1], reverse=True):
            if i < k:
                result[i] = key
            i += 1
        
        return result