# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        d = defaultdict(list)

        def dfs(node):

            if node.left:
                d[node.val].append(node.left.val)
                d[node.left.val].append(node.val)
                dfs(node.left)
            
            if node.right:
                d[node.val].append(node.right.val)
                d[node.right.val].append(node.val)
                dfs(node.right)
            
        dfs(root)
        print(d)
        q = deque()
        q.append(target.val)
        pop_count = 1
        seen = set()
        seen.add(target.val)
        while q and k:

            for _ in range(pop_count):
                cur = q.pop()
                for node in d[cur]:
                    if node not in seen:
                        seen.add(node)
                        q.appendleft(node)
            
            k -= 1
            pop_count = len(q)
        
        return list(q)