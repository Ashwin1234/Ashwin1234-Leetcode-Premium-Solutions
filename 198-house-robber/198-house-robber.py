class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if (len(nums) == 1):
            return max(dp)
        dp[1] = nums[1]
        if len(nums) == 2:
            return max(dp)
        dp[2] = nums[2] + max(0,dp[0])
        for i in range(3,len(nums)):
            dp[i] = nums[i] + max(dp[i-2],dp[i-3])
        print(dp)
        return max(dp)