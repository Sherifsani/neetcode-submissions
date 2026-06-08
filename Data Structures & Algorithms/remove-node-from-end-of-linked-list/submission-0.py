# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        current = head
        length = 0
        while current:
            current = current.next
            length += 1
        
        k = length - n
        current = dummy

        for _ in range(k):
            current = current.next

        current.next = current.next.next

        return dummy.next