class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        alphabets_freq_s = [0] * 26
        alphabets_freq_t = [0] * 26
        a_asci = ord('a')

        for i in s:
            idx = ord(i) - a_asci
            alphabets_freq_s[idx] += 1
        
        for j in t:
            idx = ord(j) - a_asci
            alphabets_freq_t[idx] += 1
        
        for i in range(26):
            if alphabets_freq_s[i] != alphabets_freq_t[i]:
                return False
        
        return True
