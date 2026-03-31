class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = [1] * 26
        for i in range(len(alpha)):
            alpha[i] = 97 + i

        for i, v in enumerate(alpha):
            alpha[i] = chr(v)

        alpha.extend(['0','1','2','3','4','5','6','7','8','9'])
        
        s = s.lower()
        news = ''
        for i in s:
            if i in alpha:
                news += i

        return news[::-1] == news