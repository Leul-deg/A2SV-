# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(node , _sum):
            
            if not node:
                return 
            # print(node.val)
            # print(cur)
            
            cur.append(node.val)

            dfs(node.left , _sum + node.val)
            dfs(node.right , _sum + node.val)
            if not node.left and not node.right and _sum + node.val == targetSum:
                res.append(cur.copy())
            cur.pop()

        dfs(root , 0)
        return res