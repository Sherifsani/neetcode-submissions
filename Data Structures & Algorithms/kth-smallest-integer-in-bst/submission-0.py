# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # brute approach: store all values in an array then return the Kth smallest easily
        queue = [ root ]
        arr = [ root.val ]

        while queue:
            current = queue.pop(0)
            
            if current.left:
                queue.append(current.left)
                arr.append(current.left.val)

            if current.right:
                queue.append(current.right)
                arr.append(current.right.val)
        
        arr.sort()
        return arr[k - 1]