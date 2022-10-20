class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x: x[0])
        first = intervals[0]
        count = 0
        for i in range(0, len(intervals) - 1):
            second = intervals[i+1]
            print(first, second)
            if second[0] < first[1] or second[0] == first[0]:
                if second[1] <= first[1]:
                    count = count + 1
                    first = second
                else:
                    count = count + 1
            else:
                first = second
                
        
        return count
            