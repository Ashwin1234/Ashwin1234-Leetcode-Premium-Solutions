# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, output, level):
        if node == None:
            return
        if len(output) <= level:
            output.append(node.val)
        elif len(output) > level:
            output[level] = node.val
        level = level + 1
        self.dfs(node.left, output, level)
        self.dfs(node.right, output, level)
        return 
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        level = 0
        self.dfs(root, output, level)
        return output
        