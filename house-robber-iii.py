# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        ans = 0
        def dfs(node):
            nonlocal ans

            if not node.left and not node.right:

                node.res = node.val
                one ,two = TreeNode() , TreeNode()
                one.res = 0 
                two.res = 0
                ans = max(ans,  node.res)
                return [node , one , two ]
            
            arr1 , arr2 = [] ,  [] 

            max1  , max2 = 0 , 0 

            node.res = 0 
            if node.left:

                arr1 = dfs(node.left)

                for child in arr1:

                    max1 = max(max1 , child.res)

                    if child != node.left and child != node.right:
                        node.res += child.res
                        break
            
            if node.right:

                # if node.val == 3:
                #     print("Yes i did get here")

                arr2 = dfs(node.right)

                # print(len(arr2), "the length baby")

                for child in arr2:

                    max2 = max(max2 , child.res)

                    if child != node.left and child != node.right:
                        # if node.val == 3:
                            # print("Yes i did get here as welllllllll")
                        node.res += child.res
                        break
            


            finale = arr1 + arr2 

            node.res += node.val

            finale.append(node)

            a = TreeNode()
            a.res = max1 + max2
            finale.append(a)
            finale.sort(reverse = True , key = lambda x : x.res)

            # print(ans,  max1 + max2 , finale[0].res)
            ans = max(ans,  max1 + max2 , finale[0].res , node.val)

            return finale[:3]

            
        dfs(root) 

        return ans