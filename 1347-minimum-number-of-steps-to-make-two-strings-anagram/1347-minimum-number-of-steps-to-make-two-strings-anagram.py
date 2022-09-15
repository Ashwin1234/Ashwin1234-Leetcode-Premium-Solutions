class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dict1 = {}
        dict2 = {}
        count = 0
        for ele in s:
            if ele in dict1:
                dict1[ele] = dict1[ele] + 1
            else:
                dict1[ele] = 1
        for ele in t:
            if ele in dict2:
                dict2[ele] = dict2[ele] + 1
            else:
                dict2[ele] = 1
        print(dict1)
        print(dict2)
        for key, value in dict1.items():
            if key not in dict2:
                count = count + value
            else:
                if value > dict2[key]:
                    count = count + value - dict2[key]
        return count