class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        output = []
        while(left <= right):
            if pow(nums[left],2) < pow(nums[right],2):
                output.append(pow(nums[right],2))
                right = right - 1
            else:
                output.append(pow(nums[left],2))
                left = left + 1
        print(output)
        output.reverse()
        return output