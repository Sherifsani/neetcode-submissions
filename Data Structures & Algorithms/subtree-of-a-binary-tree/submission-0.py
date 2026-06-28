# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        if not root:
            if not subRoot:
                return True
        # if not root or subRoot
        stack = [ root ]
        while stack:
            current = stack.pop()
            isSame = isSameTree(current, subRoot)
            if isSame:
                return True
            if not current:
                continue
            stack.append(current.left)
            stack.append(current.right)
        return False