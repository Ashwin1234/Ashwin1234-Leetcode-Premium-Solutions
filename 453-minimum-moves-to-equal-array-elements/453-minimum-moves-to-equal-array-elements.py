class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minimum = min(nums)
        count = 0
        for ele in nums:
            count = count + ele - minimum
        return count