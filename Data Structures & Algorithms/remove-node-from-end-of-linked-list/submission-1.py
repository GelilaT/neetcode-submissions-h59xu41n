# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return

        cur = head 
        count = 0
        while cur:
            count += 1
            cur = cur.next

        before = count - n
        newCount, curr = 0, head
        dummy = ListNode()
        curr = dummy
        while head:
            if newCount == before:
                curr.next = head.next
                break
            
            newCount += 1
            curr.next = head
            curr = curr.next
            head = head.next

        return dummy.next
        