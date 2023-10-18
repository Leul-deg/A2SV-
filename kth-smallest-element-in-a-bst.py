# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self,):
        self.res = []
        self.ans  = -1

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.k = k 

        self.dfs(root , 0 )

        return self.ans

        

        


    
    def dfs(self , node , count):
        if not node:
            return 0

        left = self.dfs(node.left, count)

        
        # self.res.append(node.val , count + left)

        right = self.dfs(node.right , count + left + 1)
        # print(left + count + 1 , "shiss")
        if left + count + 1 == self.k :
            self.ans = node.val
        
        return left + right + 1