# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kth_to_last(self, head: ListNode, k: int) -> ListNode:
        runner = current = head
        for i in range(k):
            if not runner:
                return None
            runner = runner.next

        while runner:
            current = current.next
            runner = runner.next
            
        return current
