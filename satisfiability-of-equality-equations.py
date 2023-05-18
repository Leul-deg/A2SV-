class UnionFind:

    def __init__(self):
        
        self.parent = {chr(i) : chr(i) for i in range(97 , 123)}

    
    def find_repr(self, node):

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
        parent1 , parent2 = self.find_repr(node1) , self.find_repr(node2)
        if parent2 != parent1:

            if parent1 < parent2:
                self.parent[parent2] = parent1
            
            else:
                self.parent[parent1] = parent2
        
            


        
    
    def areFamily(self, offspring1 , offspring2 ):

        return self.find_repr(offspring1) == self.find_repr(offspring2)
        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        family = UnionFind()
        for string in equations:
            a , b = string[0] , string[-1]
            if "==" in string:
                family.union(a ,b )
        
        for string in equations:
            a , b = string[0] , string[-1]
            if '!=' in string:
                if family.find_repr(a) == family.find_repr(b):
                    return False
        
        return True