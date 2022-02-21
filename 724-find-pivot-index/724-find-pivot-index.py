class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixsum = 0
        sum1 = 0
        sum1 = sum(nums)
        for i in range(0,len(nums)):
            if prefixsum == (sum1 - prefixsum - nums[i]):
                return i
            else:
                prefixsum = prefixsum + nums[i]
        return -1