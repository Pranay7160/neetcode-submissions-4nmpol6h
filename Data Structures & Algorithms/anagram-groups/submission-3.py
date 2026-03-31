class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_d = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for j in s:
                freq[ord(j) - ord('a')] += 1
            t = tuple(freq)
            freq_d[t].append(s)
        

        res = []
        for k in freq_d:
            res.append(freq_d.get(k))
        
        return res
        