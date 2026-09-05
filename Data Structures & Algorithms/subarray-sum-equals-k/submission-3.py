class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        count = 0
        for num in nums:
            prefix_sum += num

            needed_total = prefix_sum - k
            count += prefix_count[needed_total]

            prefix_count[prefix_sum] += 1
        
        return count