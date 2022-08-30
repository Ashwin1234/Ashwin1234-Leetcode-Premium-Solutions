class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1 = {}
        for ele in arr:
            if ele in dict1:
                dict1[ele] = dict1[ele] + 1
            else:
                dict1[ele] = 1
        valueSet = set(dict1.values())
        if len(dict1) == len(valueSet):
            return True
        else:
            return False
        