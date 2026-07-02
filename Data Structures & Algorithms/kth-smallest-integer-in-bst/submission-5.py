# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
          approach:
        - perform an inorder traversal on the tree
        - inorder traversel gives left -> root -> right
        - since it is a BST then the left most value would be the smallest then it's root and  left
        - Knowing this, we can decrement k each time we meet a node (from bottom up)
        - Then when k gets to zero we return that node
        '''
        arr = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k - 1]