# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carried = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            summ = l1.val + l2.val + carried
            val = summ
            carried = 0
            if summ >= 10:
                carried = 1
                val = summ % 10
            
            cur.next = ListNode(val)
            cur = cur.next
            l1, l2 = l1.next, l2.next

        while l1:
            summ = l1.val + carried
            val = summ
            carried = 0
            if summ >= 10:
                carried = 1
                val = summ % 10
            
            cur.next = ListNode(val)
            cur = cur.next
            l1 = l1.next

        while l2:
            summ = l2.val + carried
            val = summ
            carried = 0
            if summ >= 10:
                carried = 1
                val = summ % 10
            
            cur.next = ListNode(val)
            cur = cur.next
            l2 = l2.next

        if carried:
            cur.next = ListNode(carried)

        return dummy.next

            




            
