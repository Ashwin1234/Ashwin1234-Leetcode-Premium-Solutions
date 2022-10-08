class Solution:
    def jump(self, nums: List[int]) -> int:
        index = 0
        farthest = 0
        count = 0
        for i in range(0, len(nums) - 1):
            farthest = max(farthest, nums[i] + i)
            if(i == index):
                count = count + 1
                index = farthest
        return count