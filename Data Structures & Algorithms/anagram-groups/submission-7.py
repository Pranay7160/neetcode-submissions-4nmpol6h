class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_str = defaultdict(list)
        for s in strs:
            freq_str[tuple(sorted(s))].append(s)
        
        return list(freq_str.values())
