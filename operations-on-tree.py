class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.child = defaultdict(list)
        for idx , node in enumerate(parent):
            if node >= 0:
                self.child[node].append(idx)
        
        self.lockedBy = {}
        
        

    def lock(self, num: int, user: int) -> bool:
        if num not in self.lockedBy:
            self.lockedBy[num] = user
            return True
        
        return False
        

    def unlock(self, num: int, user: int) -> bool:
        if self.lockedBy.get(num , -3) == user:
            self.lockedBy.pop(num)
            return True
        
        return False
        

    def upgrade(self, num: int, user: int) -> bool:
        print(self.hasLockedAnc(num) , num , "has locked anc")
        if num not in self.lockedBy and self.hasLockedAnc(num) and self.hasLockedDes(num):
            #unlock descendants
            self.unlockDes(num)
            #lock the node
            self.lockedBy[num] = user
            return True

        
        return False
    

    def hasLockedAnc(self, node):

        while node != 0 :

            node = self.parent[node]

            if node in self.lockedBy:
                return False
        
        return True

    
    def hasLockedDes(self, node):

        def dfs(cur):
            
            if cur != node and cur in self.lockedBy:
                return True
            
            for neg in self.child[cur]:
                if dfs(neg):
                    return True
            return False
        
        return dfs(node)

    
    def unlockDes(self , node):

            def dfs(cur):
            
                
                
                for neg in self.child[cur]:
                    dfs(neg)

                if cur in self.lockedBy:
                    self.lockedBy.pop(cur)
            
            dfs(node)
                        


        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)