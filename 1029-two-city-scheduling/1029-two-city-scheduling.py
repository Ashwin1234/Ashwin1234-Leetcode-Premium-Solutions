class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        bCost = []
        count = 0
        for ele in costs:
            bCost.append([ele[0],ele[1],ele[1]-ele[0]])
        bCost = sorted(bCost, key = lambda x: x[2])
        print(bCost)
        for i in range(0, int(len(bCost)/2)):
            count = count + bCost[i][1]
        for i in range(int(len(bCost)/2), len(bCost)):
            count = count + bCost[i][0]
        return count
        