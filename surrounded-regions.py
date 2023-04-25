class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows , cols = len(board) , len(board[0])
        inbound = lambda x , y : 0<=x<rows  and 0 <= y < cols
        directions = [(-1 , 0 ) , ( 0 , -1) , (1 , 0 ) , ( 0 , 1)]
        seen = set()
        def dfs(r , c):
            if (r,c) in seen or board[r][c] == "X":
                return 
            
            seen.add((r,c))
            for dx , dy in directions:
                if inbound(r + dx , c + dy):
                    dfs(r + dx , c + dy)
        
        for i in range(rows):
            dfs(i , 0)
            dfs(i ,  cols - 1)
        
        for c in range(cols):
            dfs(0 , c )
            dfs(rows - 1 ,c )
        
        for i in range(rows):
            for j in range(cols):
                if (i , j ) not in seen:
                    board[i][j] = 'X'