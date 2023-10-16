# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Intuition:
        1. Maintain two pointers prev and current
        2. go till the end then current.next = prev and decrease the prev and current by one node
        '''
        current = head
        previous = None

        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        return previous