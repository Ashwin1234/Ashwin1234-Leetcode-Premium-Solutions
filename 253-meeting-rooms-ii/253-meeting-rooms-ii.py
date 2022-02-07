from heapq import heappush,heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key = lambda x:x[0])
        heap = []
        heappush(heap,intervals[0][1])
        for i in range(1,len(intervals)):
            ele = heappop(heap)
            if ele <= intervals[i][0]:
                ele = intervals[i][1]
            else:
                heappush(heap,intervals[i][1])
            heappush(heap,ele)
        return len(heap)
        
        
        