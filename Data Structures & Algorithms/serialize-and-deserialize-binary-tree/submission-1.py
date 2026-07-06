class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"

        res = []
        queue = [root]

        while queue:
            current = queue.pop(0)

            if current:
                res.append(str(current.val))
                # ALWAYS append children, even if they are None
                queue.append(current.left)
                queue.append(current.right)
            else:
                # If current is None, we just record "N" 
                # Crucially, we do NOT append more Nones to the queue!
                res.append("N")
                
        # Join with commas to handle multi-digit/negative numbers safely
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N" or not data:
            return None
        
        # Split by comma so "12" stays "12" and "-5" stays "-5"
        vals = data.split(",")
        
        root = TreeNode(int(vals[0]))
        queue = [root]
        i = 1  # Pointer to track the next child value in 'vals'
        
        while queue and i < len(vals):
            current = queue.pop(0)
            
            # Process left child
            if vals[i] != 'N':
                left_node = TreeNode(int(vals[i]))
                current.left = left_node
                queue.append(left_node)
            i += 1
            
            if i >= len(vals):
                break
                
            # Process right child
            if vals[i] != 'N':
                right_node = TreeNode(int(vals[i]))
                current.right = right_node
                queue.append(right_node)
            i += 1
            
        return root