class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key = lambda x: x[1])
        count = 1
        end = points[0][1]
        for i in range(1,len(points)):
            if end >= points[i][0]:
                continue
            else:
                count = count + 1
                end = points[i][1]
        return count
                
                
                
        