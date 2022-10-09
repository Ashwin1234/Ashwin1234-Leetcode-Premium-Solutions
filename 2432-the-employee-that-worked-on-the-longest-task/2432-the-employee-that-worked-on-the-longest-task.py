class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        task = []
        output = []
        max_task = -1
        task.append((logs[0][0], logs[0][1]))
        for i in range(1, len(logs)):
            task.append((logs[i][0], logs[i][1] - logs[i-1][1]))
        for ele in task:
            if ele[1] > max_task:
                max_task = ele[1]
        for ele in task:
            if ele[1] == max_task:
                output.append((ele[0], ele[1]))
        output = sorted(output, key = lambda x: x[0])
        return output[0][0]