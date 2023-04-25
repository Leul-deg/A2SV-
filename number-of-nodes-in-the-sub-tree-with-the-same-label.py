class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        seen = set()
        def add(arr1 , arr2):
            ans = []
            for i in range(len(arr1)):
                ans.append(arr1[i] + arr2[i])
            
            return ans

        res = [0]*n
        c = {}
        adj = defaultdict(list)
        for parent , child in edges:
            adj[parent].append(child)
            adj[child].append(parent)
        
        def dfs(node):
            seen.add(node)

            freq = [0]*26
            for neg in adj[node]:
                if neg not in seen:
                    a = dfs(neg)
                    freq = add(a , freq)
            
            letter_index = ord(labels[node]) - 97
            freq[letter_index] += 1
            res[node] = freq[letter_index]

            return freq
        
        dfs(0)

        return res