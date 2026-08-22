class Node:
    def __init__(self, n):
        self.val = n
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def getPrev(self, index):
        cur = self.head
        for _ in range(index):
            cur = cur.next

        return cur

    def get(self, index: int) -> int:
        
        if self.size <= index:
            return -1

        return self.getPrev(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if self.size < index:
            return

        prev = self.getPrev(index)
        node = Node(val)
        node.next = prev.next
        prev.next = node
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        
        if self.size <= index:
            return 

        prev = self.getPrev(index)
        prev.next = prev.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)