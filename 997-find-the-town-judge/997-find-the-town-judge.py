class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        dict1 = {}
        for i in range(1, n+1):
            dict1[i] = [0,0]
        for ele in trust:
            dict1[ele[0]][0] = dict1[ele[0]][0] + 1
            dict1[ele[1]][1] = dict1[ele[1]][1] + 1
        for key, value in dict1.items():
            if value[0] == 0 and value[1] == n-1:
                return key
        return -1
        
                
        