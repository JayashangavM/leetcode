class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            s = str(x)
            return s == s[::-1]
        return False