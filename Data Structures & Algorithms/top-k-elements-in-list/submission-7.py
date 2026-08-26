class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = []

        for key, i in sorted(count.items(), key=lambda x:x[1], reverse=True):
            if len(ans) >= k:
                break
            ans.append(key)

        return ans