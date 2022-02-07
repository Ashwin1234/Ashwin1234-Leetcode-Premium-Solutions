from heapq import heappush,heappop
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = []
        cost = 0
        for ele in sticks:
            heappush(heap,ele)
        while(len(heap) > 1):
            ele1 = heappop(heap)
            ele2 = heappop(heap)
            cost = cost + ele1 + ele2
            heappush(heap,ele1+ele2)
        return cost
            
        
        