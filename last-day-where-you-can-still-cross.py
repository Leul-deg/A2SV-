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
        # print(parent1 , parent2 , "parent1 and parent2")
        if parent2 != parent1:

            if parent1 < parent2:
                self.size[parent1] += self.size[parent2]
                self.parent[parent2] = parent1
            
            else:
                self.size[parent2] += self.size[parent1]
                self.parent[parent1] = parent2
        
    
    def areFamily(self, node1 , node2):

        return self.root(node1) == self.root(node2)
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        index =  {}
        idx = 1
        for r in range(1 , row+1):
            for c in range(1 , col+1):
                index[(r , c )] = idx 
                idx += 1
        # print(idx, "the indx")
        fin = idx + 1
        family = UnionFind(idx + 2)
        directions = [(1,  0) , (0 , 1)  , (-1 , 0) , (0 , -1)]
        clear = set()
        cells.reverse()
        for idx , tup in enumerate(cells):
            x, y = tup
            cur = index[(x , y)]
            if x  == 1:
                family.union(cur , 0)
            if x  == row:
                family.union(cur , fin)

            for dx , dy in directions:

                if (x + dx, y + dy) in clear:
                    nex = index[(x + dx , y + dy)]
                    if x + dx == 1:
                        family.union(nex , 0)
                    if x + dx == row:
                        family.union(nex , fin)
                    family.union(cur , nex)

            
            clear.add((x , y ))
            if family.areFamily(0 , fin):
                return len(cells) - idx -1
        return idx