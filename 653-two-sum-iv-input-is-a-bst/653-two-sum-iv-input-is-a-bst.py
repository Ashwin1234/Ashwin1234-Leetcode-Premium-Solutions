# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, temp):
        if root==None:
            return
        self.inorder(root.left, temp)
        temp.append(root.val)
        self.inorder(root.right, temp)
        return
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        temp = []
        self.inorder(root,temp)
        left = 0
        right = len(temp) - 1
        while(left < right):
            if temp[left] + temp[right] == k:
                return True
            elif temp[left] + temp[right] > k:
                right = right - 1
            else:
                left = left + 1
        return False
        
        