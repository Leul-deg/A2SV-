class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent = {}
        size = {}
        def union(left , right):

            if find_repr(left) == find_repr(right):
                return
            
            left = find_repr(left)
            right = find_repr(right)

            if left > right :

                parent[left]  = right 
            
            else :
                parent[right] = left
            
        
        def find_repr(node):

            hold = node

            while node != parent[node]:
                node = parent[node]
            
            while hold != node :

                temp = parent[hold]

                parent[hold] = node

                hold = temp
            
            return node 
        

        for val in range(ord('a') , ord('z')  + 1):
            parent[chr(val)] = chr(val)
            size[chr(val)] = 1
        

        for idx in range(len(s1)):

            union(s1[idx] , s2[idx])
        
        ans = []

        for char in baseStr:

            ans.append(find_repr(char))
        
        return "".join(ans)