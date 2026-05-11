# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = slow = head
        while slow and slow.next:

            fast = fast.next
            slow = slow.next.next
            if fast == slow:
                return True

        return False
        