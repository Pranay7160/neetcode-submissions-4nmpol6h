class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)

        for i, n in enumerate(numbers):
            rem = target - n
            if mp.get(rem):
                return [mp.get(rem), i+1]

            mp[n] = i + 1
        
        return []
        