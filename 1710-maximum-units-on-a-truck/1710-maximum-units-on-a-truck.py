class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key = lambda x:x[1], reverse=True)
        size = truckSize
        maxUnits = 0
        for i in range(0, len(boxTypes)):
            size = size - boxTypes[i][0]
            maxUnits = maxUnits + (boxTypes[i][0] * boxTypes[i][1])
            if size == 0:
                return maxUnits
            elif size<0:
                maxUnits = maxUnits - (abs(size) * boxTypes[i][1])
                return maxUnits
        return maxUnits