class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        output = []
        for ele in arr:
            heap.append((abs(ele - x), ele))
        heapq.heapify(heap)
        for i in range(0, k):
            res = heapq.heappop(heap)
            output.append(res[1])
        return sorted(output)