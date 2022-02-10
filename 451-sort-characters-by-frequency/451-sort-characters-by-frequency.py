from collections import OrderedDict
class Solution:
    def frequencySort(self, s: str) -> str:
        dict1 = OrderedDict()
        for ele in s:
            if ele in dict1:
                dict1[ele] = dict1[ele] + 1
            else:
                dict1[ele] = 1
        print(dict1)
        dict1 = dict(sorted(dict1.items(), key = lambda x:x[1],reverse = True))
        str1 = ""
        for key,ele in dict1.items():
            for i in range(ele):
                str1 = str1 + key
        return str1