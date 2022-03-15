class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_res = ""
        for i in range(0,len(s)):
            left = i
            right = i
            count = 1
            res = ""
            while(left >= 0 and right <= len(s) - 1):
                if s[left] == s[right]:
                    res = s[left:right+1]
                    if len(res) > len(max_res):
                        max_res = res
                else:
                    break
                left = left - 1
                right = right + 1
            
            left = i
            right = i + 1
            res = ""
            while(left >=0 and right <= len(s) - 1):
                if s[left] == s[right]:
                    res = s[left:right+1]
                    if len(res) > len(max_res):
                        max_res = res
                else:
                    break
                left = left - 1
                right = right + 1
        return max_res
        