class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s) - 1
        while l < r: 
            if s[l] != s[r]:
                return self.check_palindrome(s, l, r - 1) or self.check_palindrome(s ,l + 1, r)
            l += 1
            r -= 1

        return True
    
    def check_palindrome(self, s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True


        