# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        slow = slow.next
        slow = self.reverseLinkedlist(slow)
        while slow:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True
    
    def reverseLinkedlist(self, head):
        if not head or not head.next:
            return head
        
        dummy = ListNode(-1)
        while head:
            tmp = head
            head = head.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next
            
        
        