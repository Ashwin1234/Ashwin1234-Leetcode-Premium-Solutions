class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        dict1 = {}
        output = [0,0]
        for ele in nums:
            if ele in dict1:
                dict1[ele] = dict1[ele] + 1
            else:
                dict1[ele] = 1
                
        for ele in dict1:
            if dict1[ele] == 2:
                output[0] = output[0] + 1
                dict1[ele] = 0
            if dict1[ele] > 2:
                while(dict1[ele] >=2 ):
                    dict1[ele] = dict1[ele] - 2
                    output[0] = output[0] + 1
        
        for ele in dict1:
            if dict1[ele] == 1:
                output[1] = output[1] + 1
        return output
        
                
                