# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # def dfs(p_node, q_node):
        #     if p_node == q_node == None:
        #         return True
        #     if p_node != q_node or p_node.val != q_node.val:
        #         return False
        #     if p_node.val == q_node.val:
        #         return True
            
        if p == q == None:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        res = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return res