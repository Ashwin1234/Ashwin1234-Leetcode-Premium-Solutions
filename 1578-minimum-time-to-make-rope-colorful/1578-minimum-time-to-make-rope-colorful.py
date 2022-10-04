class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        first = 0
        second = 0
        output = 0
        while(first < len(neededTime) and second < len(neededTime)):
            sum1 = 0
            max1 = 0
            while(second < len(neededTime) and colors[first] == colors[second]):
                sum1 = sum1 + neededTime[second]
                max1 = max(max1, neededTime[second])
                second = second + 1
            output = output + sum1 - max1
            first = second
        return output