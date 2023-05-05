# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        prev = dummy
        t = 1
        for node in lists:
            if node:
                heappush(heap , (node.val , t , node))
            
            t += 1
        
        while heap :
            _ , _ , node  =  heappop(heap)

            prev.next = node

            prev = node

            node = node.next
            if node:
                heappush(heap , (node.val , t  , node))

            t += 1
        
        
        return dummy.next