class Solution:
    def knightDialer(self, n: int) -> int:

        MOD = 10 ** 9 + 7
        graph = {
            1: [6, 8],
            2: [7, 9],
            3: [8, 4],
            4: [0, 3, 9],
            5: [],
            6: [7, 0, 1],
            7: [2, 6],
            8: [1, 3],
            9: [4, 2],
            0: [6, 4]

        }

        @cache
        def dfs(node, elem):
            # print(node, elem)
            if elem == 1:
                return 1
            
            
          
            res = 0
            for neg in graph[node]:

                r =  dfs(neg , elem - 1) 

                res += r 

                res = res % MOD
            
            return res 

        ans = 0
        for num in range(10):
            if num == 5 and n != 1:
                continue
            ans += (dfs(num, n) % MOD)
        return ans % MOD