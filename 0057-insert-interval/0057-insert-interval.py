class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:            
        output = []
        if len(intervals) == 0:
            output.append(newInterval)
            return output
        for i in range(0, len(intervals)):
            if intervals[i][0] <= newInterval[0]:
                output.append(intervals[i])
            else:
                break
        if len(output) == 0:
            output.append(newInterval)
        
        if newInterval[0] <= output[-1][1]:
            output[-1] = [output[-1][0], max(output[-1][1], newInterval[1])]
        else:
            output.append(newInterval)
        
        print(output)
        
        while(i < len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1] = [output[-1][0], max(output[-1][1], intervals[i][1])]
            else:
                output.append(intervals[i])
            i = i + 1
        
        return output
            