# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if root is null return an empty array
        if not root:
            return []
        
        # we use a queue to keep track of each node as we traverse the tree (BFS)
        queue = [ root ]
        res = [[root.val]]

        while len(queue) > 0:
            arr = []
            n = len(queue)

            # at each level of the tree, iterate and add all nodes to an array
            for i in range(n):
                current = queue.pop(0)
                if current.left:
                    arr.append(current.left.val)
                    queue.append(current.left)
                if current.right:
                    arr.append(current.right.val)
                    queue.append(current.right)
                    
            # store the array in res
            res.append(arr)
        return res[:-1]