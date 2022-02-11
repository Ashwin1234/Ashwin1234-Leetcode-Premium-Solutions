class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = [0] * len(s)
        ones = 0
        zeroes = 0
        for i in range(0,len(s)):
            if s[i] == '1':
                ones = ones + 1
        ans = min(ones,len(s) - ones)
        
        count1 = 0
        for i in range(0,len(s)):
            if s[i] == '1':
                count1 = count1 + 1
            count0 = (len(s) - i - 1) - (ones - count1)
            dp[i] = count1 + count0
        return min(min(dp),ans)
        