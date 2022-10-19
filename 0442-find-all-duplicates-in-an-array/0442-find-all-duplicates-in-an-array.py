class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        temp_set = set()
        output = []
        for ele in nums:
            if ele in temp_set:
                output.append(ele)
            else:
                temp_set.add(ele)
        return output
                
        