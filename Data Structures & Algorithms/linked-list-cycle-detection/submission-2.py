# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        slow = head
        fast = head.next
        while (fast!=None and fast.next!=None):
            if (fast == slow):
                return True
            slow = slow.next
            fast = fast.next.next
        return False