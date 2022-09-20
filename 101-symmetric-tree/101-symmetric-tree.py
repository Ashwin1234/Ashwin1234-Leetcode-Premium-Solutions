# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetry(self, left, right, output):
        print(output)
        if (left == None and right != None) or (left != None and right == None):
            output = False
            return output
        if left == None and right == None:
            return output
        if left.val != right.val:
            output = False
            return output
        output = self.checkSymmetry(left.left, right.right, output)
        output = self.checkSymmetry(left.right, right.left, output)
        return output
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        output = True
        output = self.checkSymmetry(root.left, root.right, output)
        return output
        