class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = s.lower()

        l = 0
        r = len(s) - 1
        
        def is_palindrome(l, r):
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                elif not s[r].isalnum():
                    r -= 1
                elif not s[l].isalnum():
                    l += 1
                else:
                    return False
            return True
        
        while l < r:
            if s[l] != s[r]:
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)

            l += 1
            r -= 1
        return True
