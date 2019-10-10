# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def remove_dups(self, head: ListNode) -> ListNode:
        if not head:
            return head

        current = head
        seen = set([current.val])

        while current.next:
            if current.next.val in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.val)
                current = current.next

        return head


    def remove_dups2(self, head: ListNode) -> ListNode:
        if not head:
            return head

        current = head
        while current:
            runner = current
            while runner.next:
                if runner.next.val == current.val:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

        return head