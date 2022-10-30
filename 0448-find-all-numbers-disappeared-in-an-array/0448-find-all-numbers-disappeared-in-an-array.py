class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_set = set(nums)
        output = []
        for i in range(1, n+1):
            if i not in nums_set:
                output.append(i)
        
        return output
        
        