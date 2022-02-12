class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        dict1 = {}
        count = 0
        while(j<len(s)):
            if s[j] not in dict1:
                dict1[s[j]] = j
            else:
                i = max(dict1[s[j]]+1,i)
                dict1[s[j]] = j
            count = max(count,j-i+1)
           
            j = j + 1
            
        return count 
        
        