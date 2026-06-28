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
        
        # If the main tree is empty, it can only match if subRoot is also empty
        if not root:
            return not subRoot
            
        stack = [root]
        while stack:
            current = stack.pop()
            
            # 1. Guard against None immediately after popping
            if not current:
                continue
            
            # 2. Check if the trees match starting at 'current'
            if isSameTree(current, subRoot):
                return True
            
            # 3. Safe to push children now because we know 'current' is not None
            stack.append(current.left)
            stack.append(current.right)
            
        return False