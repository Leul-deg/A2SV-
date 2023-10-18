# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        # print(l1.val , l2.val , "hello")

        prev =  None
        carry = 0 
        while l1 or l2 or carry:

            one = l1.val if l1 else 0 
            two = l2.val if l2 else 0 

            cur_digit = one + two + carry

            carry = cur_digit // 10

            cur_digit = cur_digit % 10

            cur_node = ListNode(cur_digit)

            cur_node.next = prev

            prev = cur_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # cur_node = self.reverse(cur_node)

        # return cur_node


        return cur_node







    def reverse(self, node):

        prev = None

        while node :
            nex = node.next
            node.next = prev 
            prev = node
            node  = nex
        
        return prev