class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arrayset = set(nums)
        max1 = 0
            
        for ele in nums:
            if ele - 1 not in arrayset:
                curmax = 1
                while ele + 1 in arrayset:
                    ele = ele + 1
                    curmax = curmax + 1
                max1 = max(max1, curmax)
        
        return max1