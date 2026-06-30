# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = [ root ]
        res = [[root.val]]
        while len(queue) > 0:
            arr = []
            n = len(queue)
            for i in range(n):
                current = queue.pop(0)
                if current.left:
                    arr.append(current.left.val)
                    queue.append(current.left)
                if current.right:
                    arr.append(current.right.val)
                    queue.append(current.right)

            res.append(arr)
        return res[:-1]