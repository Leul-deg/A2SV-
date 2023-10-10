# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
         
            last = float('-inf')
            
            def in_order(node):
                
                nonlocal last
                # print(last)
                if not node:
                    return True
                a  = in_order(node.left)
                
                b = node.val > last
                
                last = max(node.val , last)
                
                c= in_order(node.right)
                
                return a and b and c
            
            return in_order(root)