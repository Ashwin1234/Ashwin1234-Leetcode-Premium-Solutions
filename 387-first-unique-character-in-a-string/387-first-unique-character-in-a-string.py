from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = OrderedDict()
        for ele in s:
            if ele in dict1:
                dict1[ele] = dict1[ele] + 1
            else:
                dict1[ele] = 1
        ele = -1
        for key,values in dict1.items():
            if values == 1:
                ele = key
                break
        if ele == -1:
            return -1 
        for i in range(0,len(s)):
            if s[i] == ele:
                return i
        return -1
        