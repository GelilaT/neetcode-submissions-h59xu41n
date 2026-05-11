# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        left = 0
        while l1 and l2:
            summ = l1.val + l2.val
            curr.next = ListNode((summ + left) % 10)
            curr = curr.next
            left = (summ + left) // 10

            l1 = l1.next
            l2 = l2.next

        while l1:
            temp = l1.val
            l1.val = (l1.val + left) % 10
            left = (temp + left) // 10
            curr.next = l1
            curr = curr.next
            l1 = l1.next

        while l2:
            temp = l2.val
            l2.val = (l2.val + left) % 10
            left = (temp + left) // 10
            curr.next = l2
            curr = curr.next
            l2 = l2.next

        if left:
            leftVal = ListNode(left)
            curr.next = leftVal

        return dummy.next


        