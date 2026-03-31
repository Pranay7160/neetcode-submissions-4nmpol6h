class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        smallest_str = strs[0]
        for s in strs:
            if len(s) < len(smallest_str):
                smallest_str = s

        for s in range(len(smallest_str)):
            for j in strs:
                s_str = smallest_str[:len(smallest_str)-s]
                if s_str in j:
                    if len(s_str) > len(longest):
                        longest = s_str
                else:
                    longest = ""
                    break
        
        return longest


        