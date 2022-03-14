class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(0,len(s)):
            
            left = i
            right = i
            while(left >= 0 and right <= len(s) - 1):
                if (s[left] == s[right]):
                    count = count + 1
                else:
                    break
                left = left - 1
                right = right + 1
            left = i 
            right = i + 1
            while(left >=0 and right <= len(s) -1):
                if (s[left] == s[right]):
                    count = count + 1
                else:
                    break
                left = left - 1
                right = right + 1
        
        return count
        