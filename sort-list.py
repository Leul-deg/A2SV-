# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        the_list = []
        current = head
        while current:
            the_list.append(current)
            current  = current.next
        the_list.sort(key = lambda x: x.val)
        
        for i in range(len(the_list)-1):
            the_list[i].next  = the_list[i+1]
        print(len(the_list))
        the_list[len(the_list)-1].next = None
        return the_list[0]