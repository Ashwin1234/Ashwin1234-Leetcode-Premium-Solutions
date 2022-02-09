from collections import OrderedDict
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dict1 = OrderedDict()
        count = 0
        for ele in arr:
            if ele in dict1:
                dict1[ele] = dict1[ele] + 1
            else:
                dict1[ele] = 1
        dict1 = dict(sorted(dict1.items(),key = lambda x:x[1]))
        print(dict1)
        for key,value in dict1.items():
            for i in range(value):
                if k == 0:
                    break
                dict1[key] = dict1[key] - 1
                k = k - 1
        for key,value in dict1.items():
            if value > 0:
                count = count + 1
        return count
        
            
    def getKey(self,val,dict1):
        for key,value in dict1.items():
            if value == val:
                return key
                
        
        