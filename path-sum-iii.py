# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def rec(node , prev = 0):
            if not node:
                return 
            
            node.val = prev + node.val
            
            rec(node.left , node.val)
            rec(node.right , node.val)
            
            # print(node.val)
        
        rec(root)
        hashmap = {0 : 1}
        res = 0
        def count(node):
            nonlocal res
            if not node:
                return
            
            need = node.val - targetSum
            res += hashmap.get(need , 0)
            hashmap[node.val] = hashmap.get(node.val , 0 ) + 1
            count(node.left)
            count(node.right)
            
            hashmap[node.val] = hashmap.get(node.val)  - 1
        
        count(root)
        
        return res