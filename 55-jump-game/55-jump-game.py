class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max1 = nums[0]
        for i in range(0,len(nums)):
            max1 = max(max1,i + nums[i])
            if max1>=len(nums) - 1:
                return True
            if i == max1:
                return False
        return False
        
        