class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        s = "".join(e for e in s if e.isalnum())
        l = len(s)
        for i in range(l//2):
            e = l - 1 - i
            if s[i] != s[e]:
                return False
        return True