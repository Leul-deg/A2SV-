# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        pop_count = 1
        q.append(root)
        averages =  []
        while q:
            # print()
            # cur_ave = 0 
            total  =0 
            for _ in range(pop_count):

                cur = q.popleft()
                # print(cur.val , end = " ")
                total += cur.val
                if cur.left:
                    q.append(cur.left)
                
                if cur.right:
                    q.append(cur.right)
            
            averages.append(total / pop_count)
            pop_count = len(q)
        
        return averages