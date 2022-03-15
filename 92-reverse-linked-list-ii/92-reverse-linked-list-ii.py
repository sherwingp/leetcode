# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        current, previous = head, None
        i = 0
        
        while current is not None and i < left - 1:
            previous = current
            current = current.next
            i += 1

        last_node_left = previous
        last_node_sub = current
        next = None

        i = 0
        while current is not None and i < right - left + 1:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        if last_node_left is not None:
            last_node_left.next = previous
        else:
            head = previous
        
        last_node_sub.next = current
        print(last_node_sub)
        return head