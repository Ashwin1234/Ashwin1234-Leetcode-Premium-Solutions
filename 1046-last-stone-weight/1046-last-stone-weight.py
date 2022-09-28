import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(0, len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        while(len(stones) > 1):
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 < stone2:
                heapq.heappush(stones, stone1 - stone2)
            print(stones)
        if len(stones) == 0:
            return 0
        if stones[0] < 0:
            return -1 * heapq.heappop(stones)
        return heapq.heappop(stones)