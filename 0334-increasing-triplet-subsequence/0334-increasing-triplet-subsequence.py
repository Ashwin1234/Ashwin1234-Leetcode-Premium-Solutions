class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for ele in nums:
            if ele > second:
                return True
            if ele < first:
                first = ele
            elif ele > first and ele < second:
                second = ele
        return False
            
        