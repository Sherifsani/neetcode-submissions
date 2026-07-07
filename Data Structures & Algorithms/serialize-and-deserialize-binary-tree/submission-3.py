# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return 'N'
        
        res = []
        queue = [root]
        while queue:
            current = queue.pop(0)
            if current:
                res.append(str(current.val))
                queue.append(current.left)
                queue.append(current.right)
            else:
                res.append("N")
        
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data or data == 'N':
            return None
            
        arr = data.split(",")

        root = TreeNode(int(arr[0]))
        queue = [root]
        i = 1

        while queue and i < len(arr):
            current = queue.pop(0)

            if arr[i] != 'N':
                left_node = TreeNode(int(arr[i]))
                current.left = left_node
                queue.append(left_node)
            i += 1
            
            if i >= len(arr):
                break
            
            if arr[i] != 'N':
                right_node = TreeNode(int(arr[i]))
                current.right = right_node
                queue.append(right_node)
            i += 1
        return root
            

