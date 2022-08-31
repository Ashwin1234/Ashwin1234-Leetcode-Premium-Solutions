class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        for ele in nums:
            if ele > 0:
                count = count + 1
        return count
        