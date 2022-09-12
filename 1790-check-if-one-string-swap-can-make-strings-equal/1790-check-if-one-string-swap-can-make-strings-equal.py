class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        misCount = 0
        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                misCount = misCount + 1
        if misCount > 2:
            return False

        else:
            dict1 = {}
            dict2 = {}
            for ele in s1:
                if ele in dict1:
                    dict1[ele] = dict1[ele] + 1
                else:
                    dict1[ele] = 1

            for ele in s2:
                if ele in dict2:
                    dict2[ele] = dict2[ele] + 1
                else:
                    dict2[ele] = 1
            for ele in dict1:
                if ele not in dict2:
                    return False
                else:
                    if dict1[ele] != dict2[ele]:
                        return False
        return True
        
        
                    
        