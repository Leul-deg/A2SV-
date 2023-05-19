class UnionFind:

    def __init__(self, size : int):
        self.parent = [i for i in range(size + 1)]
        self.size = [ 1 for _ in range( size + 1)]
    
    def root(self, node):

        hold =  node
        while node != self.parent[node]:
            node = self.parent[node]

        #path compression
        while hold != node:

            temp = self.parent[hold]
            self.parent[hold] = node
            hold = temp
        
        return node
    
    def union(self, node1 , node2):

        #union by size..
        parent1 , parent2 = self.root(node1) , self.root(node2)
        if parent2 != parent1:

            if self.size[parent1] > self.size[parent2]:
                self.size[parent1] += self.size[parent2]
                self.parent[parent2] = parent1
            
            else:
                self.size[parent2] += self.size[parent1]
                self.parent[parent1] = parent2
        
    
    def areFamily(self, node1 , node2):

        return self.root(node1) == self.root(node2)

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        indexs = {}


        d = {1 : [(0 , -1 , 4) , (0 , 1 , 3) , (0 , 1 , 5) , ( 0 , -1 , 6) , (0 , -1 , 1) , (0 , 1 , 1)] , 
             2 : [(-1 , 0  , 3) , (-1 , 0  , 4) , ( 1 , 0 , 5) , ( 1 , 0 , 6) , (-1 , 0 , 2) , (1, 0 , 2)], 
             3 : [ (1 , 0  , 5) , ( 1,  0 , 6) , (0 , -1 , 4) , (0 , -1 , 6)],
             4 : [(0 , 1 , 5) , (1 , 0 , 5)  , (1 , 0 , 6)],
             5 : [( 0 , -1 , 6)]


        }

        rows  , cols = len(grid) , len(grid[0])
        idx = 0 
        for r in range(rows):
            for c in range(cols):
                indexs[(r ,c )] = idx
                idx += 1
        

        inbound = lambda x , y : 0 <= x < rows and 0 <= y < cols

        family = UnionFind(len(grid[0]) * len(grid))


        for r in range(len(grid)):
            for c in range(len(grid[0])):

                key = grid[r][c]

                if key in d:
                    # print("up here")
                    for dx , dy , target in d[key]:
                        a = inbound(r + dx , c  + dy)
                        # print(a , "bad boy")
                        if inbound(r + dx , c + dy) and target == grid[r + dx][c + dy]:
                            i , j  =   indexs[(r , c)] , indexs[(r + dx , c + dy)]
                            family.union(i , j)
                            # print("we are famly")
        
        return family.areFamily(indexs[(rows - 1 , cols - 1)] , indexs[(0  , 0)])