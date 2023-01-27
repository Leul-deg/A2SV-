class Node:
    def __init__(self, value = 0 , next = None):
        self.val = value
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.dummy = Node()
        self.size = 0
        

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        cur = self.dummy.next
        for idx in range(index):
            cur = cur.next
        
        return cur.val
            
        

    def addAtHead(self, val: int) -> None:
        new  = Node(val)
        new.next = self.dummy.next
        self.dummy.next = new
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        cur = self.dummy
        for idx in range(self.size):
            cur = cur.next
        cur.next = Node(val)
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        cur = self.dummy
        for idx in range(index):
            cur = cur.next
            
        
        new = Node(val)
        new.next = cur.next 
        cur.next = new 
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >=self.size:
            return -1
        cur = self.dummy
        for idx in range(index):
            cur = cur.next
        
        cur.next = cur.next.next if cur.next else None
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)