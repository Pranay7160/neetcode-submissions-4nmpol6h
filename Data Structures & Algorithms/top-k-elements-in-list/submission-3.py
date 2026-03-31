class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ So the idea of the question is to find out the K most frequent items and not "Which element is K times repeated"."""
        nums_freq = {}
        for i in nums:
            nums_freq[i] = nums_freq.get(i, 0) + 1
        
        frequencyOfKeys = dict(sorted(nums_freq.items(), key=lambda tupleItem:tupleItem[1], reverse=True))

        return list(frequencyOfKeys.keys())[:k]
        