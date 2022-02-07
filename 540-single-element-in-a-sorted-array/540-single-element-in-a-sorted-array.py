class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while(left <= right):
            mid = int((left + right) / 2)
            if mid == 0 or mid == len(nums) - 1:
                return nums[mid]
            
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            
            if mid%2!=0:
                if nums[mid-1] == nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid + 1] == nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return null
            
        