# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = [root]
        visited = set()
        res = 0 
        while stack:
            cur = stack[-1]
            visited.add(cur)
            if cur.left not in visited and cur.left:
                stack.append(cur.left)
            
            elif cur.right not in visited and cur.right:
                stack.append(cur.right)
            
            else:
                stack.pop()

                if len(stack) > 1 and stack[-2].val % 2 == 0:
                    res += cur.val
            
        
        return res