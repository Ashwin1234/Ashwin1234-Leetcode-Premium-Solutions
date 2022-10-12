class Solution:
    def check(self, i, j, grid):
        if i > len(grid) -1 or j > len(grid) - 1 or i < 0 or j < 0:
            return False
        return True
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        count = 0
        queue = []
        queue.append((0,0))
        count = count + 1
        if grid[len(grid) -1][len(grid) - 1] == 1 or grid[0][0] == 1:
            return -1
        while(len(queue) > 0):
            for i in range(0, len(queue)):
                ele = queue.pop(0)
                if ele[0] == len(grid) - 1 and ele[1] == len(grid) - 1:
                    return count
                for (a,b) in (0,-1),(-1,0),(0,1),(1,0),(-1,-1),(1,-1),(-1,1),(1,1):
                    na,nb = ele[0]+a, ele[1] + b
                    if(self.check(na,nb, grid)):
                        if grid[na][nb] == 0:
                            grid[na][nb] = 1
                            queue.append((na,nb))
            count = count + 1
        return -1
                            