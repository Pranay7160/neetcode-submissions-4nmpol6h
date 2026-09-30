class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = len(strs[0])
        find_smallest_str = lambda strs: min(strs, key=len)
        smallest_str = find_smallest_str(strs)

        i = 0
        lensm = len(smallest_str)
        while i < len(strs):
            # strs[i][:lensm] -> this condition is imp and easy to miss we have to compare it with similar length with smallest_str
            if smallest_str != strs[i][:lensm]:
                smallest_str = smallest_str[:lensm-1]
                lensm = len(smallest_str)
                continue
            
            i += 1
        
        return smallest_str


