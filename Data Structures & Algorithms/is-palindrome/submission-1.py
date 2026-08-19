class Solution:
    def isPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) - 1
        sl = s.lower()

        newsl = ""
        for i in sl:
            if i.isalnum():
                newsl += i

        return newsl == newsl[::-1]
            


        