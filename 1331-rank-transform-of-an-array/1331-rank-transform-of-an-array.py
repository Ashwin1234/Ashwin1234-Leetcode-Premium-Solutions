class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        setArray = list(set(arr))
        setArray.sort()
        cDict = {}
        output = []
        for i in range(0, len(setArray)):
            cDict[setArray[i]] = i + 1
            
        for i in range(0, len(arr)):
            output.append(cDict[arr[i]])
        return output
        