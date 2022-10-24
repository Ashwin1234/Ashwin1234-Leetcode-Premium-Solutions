class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        count = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = dp[i-1] + 1
        
        maximum1 = max(dp)
        for ele in dp:
            if ele == maximum1:
                count = count + 1
        
        return maximum1
        