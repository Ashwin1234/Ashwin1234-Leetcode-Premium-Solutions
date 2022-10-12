class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sum1 = 0
        nums = sorted(nums, reverse = True)
        for i in range(0, len(nums) - 2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
        