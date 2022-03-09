class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_ele = float('inf')
        max_dif = 0
        for ele in nums:
            if ele < min_ele:
                min_ele = ele
            if abs(min_ele - ele) > max_dif:
                max_dif = abs(min_ele - ele)
        if max_dif == 0:
            return -1
        else:
            return max_dif
        