class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = ""
        if sum(nums) == 0:
            return '0'
        for i in range(0,len(nums)):
            nums[i] = str(nums[i])
        for i in range(0,len(nums)):
            for j in range(i + 1,len(nums)):
                if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp
                    
        for ele in nums:
            res = res + ele
        return res
        