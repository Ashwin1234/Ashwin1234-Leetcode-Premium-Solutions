class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dict1 = {}
        for ele in stones:
            dict1[ele] = set([])
        dict1[0] = set([1])
        for i in range(0, len(stones)):
            for ele in dict1[stones[i]]:
                if stones[i] + ele in dict1:
                    if ele-1 > 0:
                        dict1[stones[i] + ele].add(ele-1)
                    dict1[stones[i] + ele].add(ele)
                    dict1[stones[i] + ele].add(ele+1)
        print(dict1)
        if len(dict1[stones[-1]]) == 0:
            return False
        return True
        