# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        small , big = min(p.val , q.val) , max(p.val , q.val)
        arr = []
        def dfs(node):
            if not node :
                return False , False 
            
            l , r = node.val == small , node.val == big

            a ,b = dfs(node.left)

            c , d = dfs(node.right)

            res = (a or c or l , r or b or d)

            if res == (True , True ) and len(arr) == 0:
                arr.append(node)
            
            return res 
        
        dfs(root)

        return arr[0]