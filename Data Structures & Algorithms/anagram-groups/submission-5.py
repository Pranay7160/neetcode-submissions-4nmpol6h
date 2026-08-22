class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_str = defaultdict(list)
        for s in strs:
            s_tup = tuple(sorted(list(s)))
            freq_str[s_tup].append(s)
        
        return list(freq_str.values())
