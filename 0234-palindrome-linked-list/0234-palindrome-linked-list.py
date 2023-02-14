# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy , head
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
        prev = None
        cur = slow.next
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur  = temp  
        cur = head
        while prev:
            if prev.val != cur.val:
                return False
            prev = prev.next
            cur = cur.next
        return True
            
            
        
        
        
        
        
        