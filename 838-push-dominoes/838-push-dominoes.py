class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        force = [0] * n
        output = ""
        f = 0
        for i in range(0, len(dominoes)):
            if dominoes[i] == 'R':
                f = n
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] = force[i] + f
        for i in range(len(dominoes) - 1, -1, -1):
            if dominoes[i] == 'L':
                f = n
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] = force[i] - f
        for ele in force:
            if ele > 0:
                output = output + 'R'
            elif ele < 0:
                output = output + 'L'
            else:
                output = output + '.'
        return output
        