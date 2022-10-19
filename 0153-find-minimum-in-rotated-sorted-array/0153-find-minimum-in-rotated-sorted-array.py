class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        if nums[len(nums) -1] > nums[0]:
            return nums[0]
        while(left <= right):
            mid = int((left + right)/2)
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            elif nums[mid] < nums[0]:
                right = mid - 1
            elif nums[mid] >= nums[0]:
                left = mid + 1
        return 0