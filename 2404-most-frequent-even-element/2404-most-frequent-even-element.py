class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dict1 = {}
        maxFreq = float('-inf')
        output = -1
        for ele in nums:
            if ele%2 == 0:
                if ele in dict1:
                    dict1[ele] = dict1[ele] + 1
                else:
                    dict1[ele] = 1
        sortedDict = OrderedDict(sorted(dict1.items()))
        for ele in sortedDict:
            if sortedDict[ele] > maxFreq:
                output = ele
                maxFreq = dict1[ele]
            elif sortedDict[ele] == maxFreq:
                continue
        return output
        
                
                
        