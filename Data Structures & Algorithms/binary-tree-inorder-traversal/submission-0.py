# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        def dfs(arr, node):
            if not node:
                return 
            
            dfs(arr, node.left)
            arr.append(node.val)
            dfs(arr, node.right)
        dfs(arr, root)
        return arr