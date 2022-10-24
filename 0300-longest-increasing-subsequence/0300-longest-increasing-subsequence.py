class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            max_temp = -1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    max_temp = max(max_temp,max(dp[i], dp[j]) + 1) 
            dp[i] = max(dp[i], max_temp)
            
        print(dp)
        
        return max(dp)
        