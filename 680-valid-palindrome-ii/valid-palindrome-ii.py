class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palindromeCheck(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l = 0 
        r = len(s) - 1

        while l < r: 
            if s[l] != s[r]:
                return palindromeCheck(s, l + 1, r) or palindromeCheck(s, l, r - 1)
            l += 1
            r -= 1
        return True
        