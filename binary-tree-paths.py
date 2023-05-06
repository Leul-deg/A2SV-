# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(node , store):

            if not node.left and not node.right:
                store = store + [str(node.val)]
                res.append("->".join(store))
            
            if node.left:
                dfs(node.left , store + [str(node.val)])
            if node.right:
                dfs(node.right , store + [str(node.val)])
        dfs(root , [])
        return res