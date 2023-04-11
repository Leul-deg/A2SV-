class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = -1*float('inf')
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0  
            
            left = dfs(node.left)
            right = dfs(node.right)

            max_sum = max(left + node.val , right + node.val , left + right + node.val , max_sum, node.val)

            return max(max(left , right) + node.val , node.val)


        dfs(root)

        return max_sum