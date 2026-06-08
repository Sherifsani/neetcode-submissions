# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for head in lists:
            current = head
            while current:
                arr.append(current.val)
                current = current.next
        
        arr.sort()
        res = ListNode()
        current = res
        for val in arr:
            temp = ListNode(val)
            current.next = temp
            current = temp
        
        return res.next