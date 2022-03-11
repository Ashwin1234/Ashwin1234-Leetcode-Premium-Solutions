class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        right = 0
        for i in range(0,len(nums)):
            if nums[i] == 0:
                left = i
                right = i + 1
                break
        while left<=right and right < len(nums):
            if nums[right] != 0:
                val = nums[left]
                nums[left] = nums[right]
                nums[right] = val
                left = left + 1
            right = right + 1
        """
        Do not return anything, modify nums in-place instead.
        """
        