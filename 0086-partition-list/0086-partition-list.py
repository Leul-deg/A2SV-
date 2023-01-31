# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return
        
        # small , big = 
        dummy_1 = small = ListNode()
        dummy_2 = big = ListNode()
        
        cur = head
        while cur:
            temp = cur.next
            if cur.val < x:
                # small.next = cur
                # small = cur
                if small:
                    small.next = cur
                small =cur
            else:
                if big:
                    big.next = cur
                big = cur
            cur.next = None
            cur = temp
            
        
        small.next = dummy_2.next
        return dummy_1.next
