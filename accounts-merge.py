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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        family = UnionFind(len(accounts))
        def same(one , two):

            return len(checker[one] & checker[two]) > 0

        d = defaultdict(list)
        checker = [set(tup[1:]) for tup in accounts]

        for idx , acc in enumerate(accounts):
            d[acc[0]].append(idx)

        for key in d:

            for i in range(len(d[key])):

                for j in range(i + 1 , len(d[key])):
                    a , b = d[key][i] , d[key][j]
                    if family.root(a) != family.root(b) and same(a  ,  b ):
                        family.union(a , b )
        
        parents = defaultdict(list)

        for idx in range(len(accounts)):
            p = family.root(idx)
            parents[p].append(idx)
        
        ans  = []

        for key in parents:

            uni = checker[parents[key][0]]
            for s in parents[key]:
                uni.update(checker[s])
            
            res = [accounts[key][0]] + sorted(list(uni))

            ans.append(res)
        
        return ans