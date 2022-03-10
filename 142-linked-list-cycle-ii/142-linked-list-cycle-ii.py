# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
       
        while fast is not None and slow is not None:
            if fast.next == None:
                return None
            fast = fast.next.next
            slow = slow.next

            
            if fast == slow:
                length = self.calculate_distance(slow)
                return self.get_start(length, head)
        return None
    
    def calculate_distance(self, slow):
        curr_length = 0
        curr = slow
        while True:
            curr = curr.next
            curr_length += 1
            if curr == slow:
                break
        return curr_length
    
    def get_start(self, length, head):
        p_1, p_2 = head, head
        for i in range(length):
            p_2 = p_2.next
        
        while p_1 is not p_2:
            p_2 = p_2.next
            p_1 = p_1.next
            
        return p_1
        
            