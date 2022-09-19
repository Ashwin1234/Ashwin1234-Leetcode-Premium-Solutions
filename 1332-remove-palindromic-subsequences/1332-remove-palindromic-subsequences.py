class Solution:
    def removePalindromeSub(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        isPal = 1
        while(left <= right):
            if s[left] != s[right]:
                isPal = 0
                break
            left = left + 1
            right = right - 1
        if isPal == 1:
            return 1
        else:
            return 2
        
        
        