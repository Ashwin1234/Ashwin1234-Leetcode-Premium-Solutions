class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dict1 = {}
        output = []
        for arrays in nums:
            for ele in arrays:
                if ele in dict1:
                    dict1[ele] = dict1[ele] + 1
                else:
                    dict1[ele] = 1
        
        for key, value in dict1.items():
            if value == len(nums):
                output.append(key)
        return sorted(output)