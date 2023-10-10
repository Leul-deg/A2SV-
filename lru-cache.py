class Node():
    """
    The nodes are basic units stored in the cache.
    """  
    def __init__(self, key, val):
        """A node has some basic attributes as below."""
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList():
    """
    The cache uses a hash map and a double linked list to implement its storage distribution strategy.
    Here is how a double linked list is implemented.
    """
    def __init__(self):
        """A double linked list has a head and a tail. Beside, it has a `size` attribute to keep track of the size of the list."""
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addNodeAtTheEnd(self, node):
        """Add a node to the end of the list, right before the tail."""
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1

    def removeNode(self, node):
        """Remove a specific node from the list."""
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def removeFirstNode(self):
        """Remove the first node (the node right after the head) and return it."""
        if self.size == 0:
            return None
        firstNode = self.head.next
        self.removeNode(firstNode)
        return firstNode

class LRUCache(object):
    """
    An LRUCache uses a hash map and a double linked list to implement its storage distribution strategy.
    So to `get` a node and `put` a node (including removing and inserting a node) will only take O(1) time complexity.
    """
    def __init__(self, capacity):
        """
        :type capacity
        """
        self.map = dict()
        self.linkedList = DoubleLinkedList()
        self.capacity = capacity

    def findNodebyKey(self, key):
        """Return the node by the key"""
        return self.map.get(key, None)

    def moveNodeToTheEnd(self, node):
        """Move one node to the end by first removing it and then inserting it."""
        self.linkedList.removeNode(node)
        self.linkedList.addNodeAtTheEnd(node)

    def updateNodeVal(self, key, val):
        """Update one node's value"""
        self.get(key)
        self.findNodebyKey(key).val = val
    
    def removeFirstNodeFromCache(self):
        """Remove the first node from the linked list and also delete its mapping."""
        firstNode = self.linkedList.removeFirstNode()
        del self.map[firstNode.key]

    def insertNewNodeInCache(self, node):
        """Insert a new node."""
        self.map[node.key] = node
        self.linkedList.addNodeAtTheEnd(node)


    def get(self, key):
        """
        :type key
        :rtype
        """
        node = self.findNodebyKey(key)
        if node != None:
            self.moveNodeToTheEnd(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key
        :type value
        :rtype: None
        """
        if key in self.map:
            self.updateNodeVal(key, value)
        else:
            if self.linkedList.size == self.capacity:
                self.removeFirstNodeFromCache()
            node = Node(key, value)
            self.insertNewNodeInCache(node)