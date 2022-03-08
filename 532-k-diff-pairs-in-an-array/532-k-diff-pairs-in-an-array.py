class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        dict1 = {}
        count = 0
        for ele in nums:
            if ele in dict1:
                dict1[ele] = dict1[ele] + 1
            else:
                dict1[ele] = 1
        print(dict1)
        for key in dict1:
            if k == 0:
                if dict1[key] >= 2:
                    count = count + 1
            elif key + k in dict1:
                count = count + 1
            
        
        return count
        